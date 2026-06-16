def is_identical(value1: object, value2: object) -> bool:
    return value1 is value2
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    identical_ref = sample_list
    different_value = list(sample_list)
    result_1 = is_identical(sample_list, identical_ref)
    result_2 = is_identical(sample_list, different_value)
    print(f"Identical reference: {result_1}")
    print(f"Different content (different object): {result_2}")