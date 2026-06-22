def find_smallest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list1 = [5, 2, 8, 1, 9]
    sample_list2 = [-10, 0, 50, -3]
    print(f"Minimum of {sample_list1}: {find_smallest_element(sample_list1)}")
    print(f"Minimum of {sample_list2}: {find_smallest_element(sample_list2)}")