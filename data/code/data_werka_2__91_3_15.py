def flip_boolean(value: bool) -> bool:
    mask: int = 1
    int_value: int = int(value)
    flipped_int: int = int_value ^ mask
    return bool(flipped_int)

if __name__ == '__main__':
    sample_true: bool = True
    sample_false: bool = False
    result_1: bool = flip_boolean(sample_true)
    result_2: bool = flip_boolean(sample_false)
    print(result_1)
    print(result_2)