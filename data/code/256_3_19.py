def find_range(data):
    if not data:
        raise ValueError("Input set cannot be empty")
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_set1 = {1, 5, 2, 8, 3}
    sample_set2 = {10, 4, 7, 1, 9}
    empty_set = set()
    single_element_set = {7}

    print(f"Range of {sample_set1}: {find_range(sample_set1)}")
    print(f"Range of {sample_set2}: {find_range(sample_set2)}")
    try:
        print(f"Range of {empty_set}: {find_range(empty_set)}")
    except ValueError as e:
        print(f"Error for empty set: {e}")
    print(f"Range of {single_element_set}: {find_range(single_element_set)}")