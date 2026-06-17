def find_min_mixed(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data:
        if item < minimum:
            minimum = item
    if isinstance(minimum, int):
        return float(minimum)
    return minimum
if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718]
    list2 = [10, -5, 20.5, 0]
    list3 = [5, 5.0, 4.99]
    list4 = [-100, 0, 100]
    list5 = [7]
    list6 = []
    print(f"Min in {list1}: {find_min_mixed(list1)}")
    print(f"Min in {list2}: {find_min_mixed(list2)}")
    print(f"Min in {list3}: {find_min_mixed(list3)}")
    print(f"Min in {list4}: {find_min_mixed(list4)}")
    print(f"Min in {list5}: {find_min_mixed(list5)}")
    try:
        find_min_mixed(list6)
    except ValueError as e:
        print(f"Error for empty list: {e}")