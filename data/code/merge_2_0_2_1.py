def is_identical(value1: object, value2: object) -> bool:
    return value1 is value2
if __name__ == '__main__':
    sample_list_a = [10, 20, 30]
    sample_list_b = [10, 20, 30]
    same_reference = sample_list_a
    result_1 = is_identical(sample_list_a, sample_list_b)
    result_2 = is_identical(sample_list_a, same_reference)
    print(f"Are lists with identical content the same object? {result_1}")
    print(f"Do references point to the exact same memory location? {result_2}")