def find_max_stable(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for i in range(1, len(data)):
        if data[i] > max_value:
            max_value = data[i]
    return max_value
if __name__ == '__main__':
    list1 = [3.14, 2.718, 1.618, 4.0]
    list2 = [-5.5, -10.2, -3.3, -1.1]
    list3 = [1.0, 1.0000000000000001, 0.9999999999999999]
    list4 = [123.456e-10, 123.457e-10, 123.455e-10]
    empty_list = []
    print(f"Max in {list1}: {find_max_stable(list1)}")
    print(f"Max in {list2}: {find_max_stable(list2)}")
    print(f"Max in {list3}: {find_max_stable(list3)}")
    print(f"Max in {list4}: {find_max_stable(list4)}")
    try:
        find_max_stable(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")