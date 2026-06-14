def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for number in data[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [-10, -5, -20, -1]
    list3 = [42]
    empty_list = []
    print(f"Largest in {list1}: {find_largest(list1)}")
    print(f"Largest in {list2}: {find_largest(list2)}")
    print(f"Largest in {list3}: {find_largest(list3)}")
    try:
        find_largest(empty_list)
    except ValueError as e:
        print(f"Handling empty list error: {e}")