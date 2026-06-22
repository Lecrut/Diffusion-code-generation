def flip_boolean(value: bool) -> bool:
    mask: int = -1
    flipped_int: int = value ^ mask
    return bool(flipped_int)

if __name__ == '__main__':
    sample_in: bool = False
    result: bool = flip_boolean(sample_in)
    print(result)
    sample_in = True
    result = flip_boolean(sample_in)
    print(result)