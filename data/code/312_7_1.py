def find_largest(arr):
    if not arr:
        raise ValueError("Input list cannot be empty")
    largest = arr[0]
    for element in arr[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    list3 = [-10, -5, -20]
    list4 = [42]
    list5 = []
    print(f"List 1: {list1}, Largest: {find_largest(list1)}")
    print(f"List 2: {list2}")
    try:
        print(f"List 2: {find_largest(list2)}")
    except ValueError as e:
        print(f"Error for List 2: {e}")
    print(f"List 3: {list3}, Largest: {find_largest(list3)}")
    print(f"List 4: {list4}, Largest: {find_largest(list4)}")
    print(f"List 5: {list5}")
    try:
        print(f"List 5: {find_largest(list5)}")
    except ValueError as e:
        print(f"Error for List 5: {e}")