def find_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for x in data[1:]:
        if x > max_val:
            max_val = x
    return max_val
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -8, -2]
    list3 = [7]
    list4 = []
    print(f"Max of {list1}: {find_max(list1)}")
    print(f"Max of {list2}: {find_max(list2)}")
    print(f"Max of {list3}: {find_max(list3)}")
    try:
        find_max(list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")