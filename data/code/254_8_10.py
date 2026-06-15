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
    list2 = [-5, 10.5, -1.2]
    list3 = [100, 50.5, 25]
    list4 = [7, 7.0, 7.1]
    list5 = [10]
    print(f"Min in {list1}: {find_min_mixed(list1)}")
    print(f"Min in {list2}: {find_min_mixed(list2)}")
    print(f"Min in {list3}: {find_min_mixed(list3)}")
    print(f"Min in {list4}: {find_min_mixed(list4)}")
    print(f"Min in {list5}: {find_min_mixed(list5)}")