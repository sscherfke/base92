# BEERWARE LICENSE
'''
base91: a library
'''
__version__ = (0, 0, 0)

def base91_chr(val):
    '''
    Map an integer value <91 to a char

    >>> base91_chr(0)
    '!'
    >>> base91_chr(1)
    '#'
    >>> base91_chr(61)
    '_'
    >>> base91_chr(62)
    'a'
    >>> base91_chr(90)
    '}'
    >>> base91_chr(91)
    Traceback (most recent call last):
        ...
    ValueError: val must be in [0, 91)
    '''
    if not isinstance(val, int):
        val = ord(val)
    if val < 0 or val >= 91:
        raise ValueError('val must be in [0, 91)')
    if val == 0:
        return '!'
    elif val <= 61:
        return chr(ord('#') + val - 1)
    else:
        return chr(ord('a') + val - 62)

def base91_ord(val):
    '''
    '''

def base91_encode(bytstr):
    '''
    Take a byte-string, and encode it in base 91

    >>> base91_encode("\\x00")
    '!!~'
    >>> base91_encode("\x01")
    '!B~'
    >>> base91_encode("aa")
    'D8-9~'
    >>> base91_encode("aaaaaaaaaaaaa")
    'D81RPya.)hgNA(%s'
    '''
    if not bytstr:
        return '~'
    # prime the pump
    bitstr = '{:08b}'.format(ord(bytstr[0]))
    bytstr = bytstr[1:]
    resstr = ''
    while len(bytstr):
        while len(bitstr) < 13 and bytstr:
            bitstr += '{:08b}'.format(ord(bytstr[0]))
            bytstr = bytstr[1:]
        i = int(bitstr[:13], 2)
        resstr += base91_chr(i / 91)
        resstr += base91_chr(i % 91)
        bitstr = bitstr[13:]
    if bitstr:
        bitstr += '0' * (13 - len(bitstr))
        i = int(bitstr, 2)
        resstr += base91_chr(i / 91)
        resstr += base91_chr(i % 91)
        resstr += '~'
    return resstr

def base92_decode(bstr):
    '''
    '''

if __name__ == "__main__":
    import doctest
    doctest.testmod()
