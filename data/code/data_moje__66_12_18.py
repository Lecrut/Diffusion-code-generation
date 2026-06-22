def km_to_m(kilometers: int) -> int:
    if not isinstance(kilometers, int):
        raise TypeError("Input must be an integer.")
    return kilometers * 1000

if __name__ == '__main__':
    sample_kilometers = 5
    result = km_to_m(sample_kilometers)
    print(result)