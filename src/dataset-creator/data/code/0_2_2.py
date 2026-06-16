def is_identical(value1: object, value2: object) -> bool:
    return value1 is value2
if __name__ == '__main__':
    sample_int = 42
    another_int = 42
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    shared_list = []
    ref_to_shared = shared_list
    print(f"Integers identical: {is_identical(sample_int, another_int)}")
    print(f"Lists identical (value): {list_a == list_b}")
    print(f"Lists identical (identity): {is_identical(list_a, list_b)}")
    print(f"Shared reference identity: {is_identical(shared_list, ref_to_shared)}")