def invert_value(target: bool) -> bool:
    mask: int = -1
    result: int = target ^ mask
    inverted: bool = bool(result & 1)
    return inverted

if __name__ == '__main__':
    sample_in: bool = True
    sample_out: bool = invert_value(sample_in)
    print(sample_out)
    sample_in_2: bool = False
    sample_out_2: bool = invert_value(sample_in_2)
    print(sample_out_2)