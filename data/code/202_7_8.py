def find_absolute_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    list1 = [-5, 10, -20, 3]
    list2 = [0, -1, -5, 0]
    list3 = [7, 7, 7, 7]
    list4 = [-100, -50, -25]
    list5 = [42]
    list6 = []
    print(f"List 1: {list1}, Largest: {find_absolute_largest(list1)}")
    print(f"List 2: {list2}, Largest: {find_absolute_largest(list2)}")
    print(f"List 3: {list3}, Largest: {find_absolute_largest(list3)}")
    print(f"List 4: {list4}, Largest: {find_absolute_largest(list4)}")
    print(f"List 5: {list5}, Largest: {find_absolute_largest(list5)}")
    try:
        find_absolute_largest(list6)
    except ValueError as e:
        print(f"List 6 Error: {e}")