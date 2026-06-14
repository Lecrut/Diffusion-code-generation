def find_max_stable(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
    return max_val
if __name__ == '__main__':
    list1 = [3.14, 2.718, 1.618, 4.0]
    list2 = [-5.5, -1.2, -8.9, -3.3]
    list3 = [1e-10, 1e-12, 1e-11]
    list4 = [0.0, -0.001, 0.0000001]
    empty_list = []
    print(f"Max of {list1}: {find_max_stable(list1)}")
    print(f"Max of {list2}: {find_max_stable(list2)}")
    print(f"Max of {list3}: {find_max_stable(list3)}")
    print(f"Max of {list4}: {find_max_stable(list4)}")
    try:
        find_max_stable(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")