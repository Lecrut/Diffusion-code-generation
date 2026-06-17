def find_min_mixed(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_val = data[0]
    for item in data:
        if item < min_val:
            min_val = item
    if isinstance(min_val, int):
        return float(min_val)
    else:
        return min_val
if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718]
    list2 = [10, -5, 20.5, 3]
    list3 = [5, 5.0, 4.99]
    list4 = [-100, 0, 1000]
    list5 = [7]
    list6 = []
    print(f"Minimum of {list1}: {find_min_mixed(list1)}")
    print(f"Minimum of {list2}: {find_min_mixed(list2)}")
    print(f"Minimum of {list3}: {find_min_mixed(list3)}")
    print(f"Minimum of {list4}: {find_min_mixed(list4)}")
    print(f"Minimum of {list5}: {find_min_mixed(list5)}")
    try:
        find_min_mixed(list6)
    except ValueError as e:
        print(f"Error for {list6}: {e}")