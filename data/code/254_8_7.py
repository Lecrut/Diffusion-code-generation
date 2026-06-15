def find_minimum(data):
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
    list3 = [10, 5, 20.5, 1]
    list4 = [3.14159, 2.71828]
    list5 = [100]
    list6 = [-10, -5.5, 0]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    print(f"Minimum of {list4}: {find_minimum(list4)}")
    print(f"Minimum of {list5}: {find_minimum(list5)}")
    print(f"Minimum of {list6}: {find_minimum(list6)}")