def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [7]
    list4 = []
    print(f"List 1: {list1}, Largest: {find_largest(list1)}")
    print(f"List 2: {list2}, Largest: {find_largest(list2)}")
    print(f"List 3: {list3}, Largest: {find_largest(list3)}")
    try:
        find_largest(list4)
    except ValueError as e:
        print(f"List 4: {list4}, Error: {e}")