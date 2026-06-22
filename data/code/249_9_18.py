def find_largest(data):
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list1 = [7, 3, 9, 5, 6, 2, 4, 8]
    sample_list2 = [-3, -9, -1, -4, -2, -5, -8, -7]
    print(f"Largest in {sample_list1}: {find_largest(sample_list1)}")
    print(f"Largest in {sample_list2}: {find_largest(sample_list2)}")