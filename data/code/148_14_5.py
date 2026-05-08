def find_largest_element(data):
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
    list3 = [7, 7, 7, 7]
    list4 = [42]
    list5 = [-100, 0, -50]
    empty_list = []
    print(f"List 1: {list1}, Largest: {find_largest_element(list1)}")
    print(f"List 2: {list2}, Largest: {find_largest_element(list2)}")
    print(f"List 3: {list3}, Largest: {find_largest_element(list3)}")
    print(f"List 4: {list4}, Largest: {find_largest_element(list4)}")
    print(f"List 5: {list5}, Largest: {find_largest_element(list5)}")
    try:
        find_largest_element(empty_list)
    except ValueError as e:
        print(f"Handling empty list error: {e}")