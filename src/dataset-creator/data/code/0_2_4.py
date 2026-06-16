def is_identical(value1: object, value2: object) -> bool:
    return value1 is value2
if __name__ == '__main__':
    sample_int_1 = 42
    sample_int_2 = 42
    sample_list_a = [10]
    sample_list_b = [10]
    shared_reference = "shared"
    print(f"Integers identical: {is_identical(sample_int_1, sample_int_2)}")
    print(f"Lists identical: {is_identical(sample_list_a, sample_list_b)}")
    print(f"Shared reference identical: {is_identical(shared_reference, shared_reference)}")