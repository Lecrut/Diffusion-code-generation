def find_range(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 10, 10]
    list3 = [-5, 0, 5, -10]
    empty_list = []
    print(f"Range of {list1}: {find_range(list1)}")
    print(f"Range of {list2}: {find_range(list2)}")
    print(f"Range of {list3}: {find_range(list3)}")
    try:
        find_range(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")