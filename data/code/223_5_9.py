def find_max_stable(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for i in range(1, len(data)):
        if data[i] > max_value:
            max_value = data[i]
    return max_value
if __name__ == '__main__':
    list1 = [3.14, 2.718, 1.618, 2.0]
    list2 = [-5.5, -1.2, -10.0, -3.3]
    list3 = [100.0, 50.0, 200.0, 150.0]
    list4 = [0.0, -1.0, 5.0, -10.0]
    empty_list = []
    print(f"Max of {list1}: {find_max_stable(list1)}")
    print(f"Max of {list2}: {find_max_stable(list2)}")
    print(f"Max of {list3}: {find_max_stable(list3)}")
    print(f"Max of {list4}: {find_max_stable(list4)}")
    try:
        find_max_stable(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")