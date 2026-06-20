def determine_outcome(a: bool, b: bool, c: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool) or (not isinstance(c, bool)):
        raise ValueError('All inputs must be boolean values.')
    return a & b | ~c
if __name__ == '__main__':
    val1 = True
    val2 = False
    val3 = True
    print(determine_outcome(val1, val2, val3))