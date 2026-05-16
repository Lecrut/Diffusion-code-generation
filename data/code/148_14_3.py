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
    list2 = [-5, -1, -10, -2]
    list3 = [7]
    list4 = [42, 42, 42]
    list5 = [0, -100, 50]
    list6 = []
    print(f"List 1: {list1}, Largest: {find_largest(list1)}")
    print(f"List 2: {list2}, Largest: {find_largest(list2)}")
    print(f"List 3: {list3}, Largest: {find_largest(list3)}")
    print(f"List 4: {list4}, Largest: {find_largest(list4)}")
    print(f"List 5: {list5}, Largest: {find_largest(list5)}")
    try:
        find_largest(list6)
    except ValueError as e:
        print(f"List 6: {list6}, Error: {e}")