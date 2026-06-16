def is_identical(value1: object, value2: object) -> bool:
    return value1 is value2
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    identical_ref = sample_list
    different_content = [10, 20, 30]
    result_1 = is_identical(sample_list, identical_ref)
    result_2 = is_identical(sample_list, different_content)
    print(f"Identical reference check: {result_1}")
    print(f"Different content check: {result_2}")