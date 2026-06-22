def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 1, 7]
    print(f"List: {sample_list1}, Largest: {find_largest(sample_list1)}")

    sample_list2 = [-3, -8, -1, -4, -6]
    print(f"List: {sample_list2}, Largest: {find_largest(sample_list2)}")

    sample_list3 = [25]
    print(f"List: {sample_list3}, Largest: {find_largest(sample_list3)}")