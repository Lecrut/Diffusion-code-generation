def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -3]
    list3 = [42]
    list4 = [7]
    empty_list = []
    print(f"Largest in {list1}: {find_largest(list1)}")
    print(f"Largest in {list2}: {find_largest(list2)}")
    print(f"Largest in {list3}: {find_largest(list3)}")
    print(f"Largest in {list4}: {find_largest(list4)}")
    try:
        find_largest(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")