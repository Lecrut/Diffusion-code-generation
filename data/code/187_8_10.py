def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for num in data:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"List: {sample_list1}, Largest element: {find_largest(sample_list1)}")
    sample_list2 = [-10, -5, -20, -1]
    print(f"List: {sample_list2}, Largest element: {find_largest(sample_list2)}")
    sample_list3 = [7]
    print(f"List: {sample_list3}, Largest element: {find_largest(sample_list3)}")
    sample_list4 = []
    print(f"List: {sample_list4}, Largest element: {find_largest(sample_list4)}")