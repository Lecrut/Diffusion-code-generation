def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [42]
    list4 = [100, 50, 25]
    empty_list = []
    print(f"Largest in {list1}: {find_largest(list1)}")
    print(f"Largest in {list2}: {find_largest(list2)}")
    print(f"Largest in {list3}: {find_largest(list3)}")
    print(f"Largest in {list4}: {find_largest(list4)}")
    try:
        find_largest(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")