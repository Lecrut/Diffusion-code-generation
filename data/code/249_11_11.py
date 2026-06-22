def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for num in data[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_list1 = [34, 78, 23, 56, 90]
    sample_list2 = [-5, -2, -8, -1, -7]
    sample_list3 = [100]

    print(f"Largest in {sample_list1}: {find_largest(sample_list1)}")
    print(f"Largest in {sample_list2}: {find_largest(sample_list2)}")
    print(f"Largest in {sample_list3}: {find_largest(sample_list3)}")