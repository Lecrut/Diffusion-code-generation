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
    list2 = [10, -5, 20, 3]
    list3 = [100.5, 99.9, 100.0]
    list4 = [-10, -50, 0, 1]
    empty_list = []
    print(f"List 1: {list1}")
    print(f"Smallest in List 1: {find_smallest_in_list(list1)}")
    print("-" * 20)
    print(f"List 2: {list2}")
    print(f"Smallest in List 2: {find_smallest_in_list(list2)}")
    print("-" * 20)
    print(f"List 3: {list3}")
    print(f"Smallest in List 3: {find_smallest_in_list(list3)}")
    print("-" * 20)
    print(f"List 4: {list4}")
    print(f"Smallest in List 4: {find_smallest_in_list(list4)}")
    print("-" * 20)
    try:
        find_smallest_in_list(empty_list)
    except ValueError as e:
        print(f"Error handling empty list: {e}")