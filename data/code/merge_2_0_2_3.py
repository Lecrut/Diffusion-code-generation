def is_identical(value1: object, value2: object) -> bool:
    return value1 is value2
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    identical_reference = sample_list
    distinct_value = list(sample_list)
    result_identity = is_identical(sample_list, identical_reference)
    result_equality = (sample_list == distinct_value)
    print(f"Identity check ([ref]: {result_identity})")
    print(f"Equality check: {result_equality}")