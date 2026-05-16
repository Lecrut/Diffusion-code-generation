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
    list2 = [-5, -1, -10, -3]
    list3 = [7]
    list4 = [42, 42, 42]
    list5 = [-100, 0, -50]
    list6 = []
    print(f"List: {list1}, Largest element: {find_largest_element(list1)}")
    print(f"List: {list2}, Largest element: {find_largest_element(list2)}")
    print(f"List: {list3}, Largest element: {find_largest_element(list3)}")
    print(f"List: {list4}, Largest element: {find_largest_element(list4)}")
    print(f"List: {list5}, Largest element: {find_largest_element(list5)}")
    try:
        find_largest_element(list6)
    except ValueError as e:
        print(f"Error for empty list: {e}")