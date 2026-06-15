def find_smallest_in_list(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty.")
    smallest = data_list[0]
    for item in data_list[1:]:
        if item < smallest:
            smallest = item
    return smallest
if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.5]
    list2 = [10, -5, 22, 8]
    list3 = [42, 33, 11, 99]
    list4 = [1.0, 5.5, 0.1, 9.9]
    empty_list = []
    print(f"List 1: {list1}")
    print(f"Smallest in List 1: {find_smallest_in_list(list1)}\n")
    print(f"List 2: {list2}")
    print(f"Smallest in List 2: {find_smallest_in_list(list2)}\n")
    print(f"List 3: {list3}")
    print(f"Smallest in List 3: {find_smallest_in_list(list3)}\n")
    print(f"List 4: {list4}")
    print(f"Smallest in List 4: {find_smallest_in_list(list4)}\n")
    try:
        find_smallest_in_list(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")