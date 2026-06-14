def find_max_mixed(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for item in data[1:]:
        if isinstance(max_val, (int, float)):
            if isinstance(item, (int, float)):
                if item > max_val:
                    max_val = item
            else:
                raise TypeError("List contains non-numeric elements")
        else:
            raise TypeError("List contains non-numeric elements")
    return max_val
if __name__ == '__main__':
    list1 = [10, 5.5, 3, 8.1]
    list2 = [-5, -10.2, -1, -20.5]
    list3 = [7, 7.0, 7.5]
    list4 = [1, 'a', 5]
    list5 = []
    try:
        print(f"Max in {list1}: {find_max_mixed(list1)}")
        print(f"Max in {list2}: {find_max_mixed(list2)}")
        print(f"Max in {list3}: {find_max_mixed(list3)}")
        print(f"Max in {list4}: {find_max_mixed(list4)}")
        print(f"Max in {list5}: {find_max_mixed(list5)}")
    except (ValueError, TypeError) as e:
        print(f"Error encountered: {e}")