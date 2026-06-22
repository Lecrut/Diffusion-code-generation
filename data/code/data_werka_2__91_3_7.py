def negate_boolean(value: bool) -> bool:
    mask: int = -1
    inverted_int: int = value ^ mask
    result: bool = bool(inverted_int)
    return result

if __name__ == '__main__':
    sample_true: bool = True
    sample_false: bool = False
    print(negate_boolean(sample_true))
    print(negate_boolean(sample_false))