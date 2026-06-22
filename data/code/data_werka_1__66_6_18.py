def compare_adjacent_numbers(data):
    n = len(data)
    if n <= 1:
        return True
    for i in range(n - 1):
        try:
            if isinstance(data[i], (int, float)) and isinstance(data[i+1], (int, float)):
                continue
            else:
                raise TypeError(f"Non-numeric elements found at indices {i} and {i+1}")
        except TypeError as e:
            print(e)
            return False
    return True

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 'a', 3, 4, 5]
    list3 = [5.0, 4.5, 3.3, 2.2, 1.1]
    list4 = [1, 1, 2, 3, 3]
    list5 = [10]
    list6 = []
    print(f"List 1 comparison result: {compare_adjacent_numbers(list1)}")
    print(f"List 2 comparison result: {compare_adjacent_numbers(list2)}")
    print(f"List 3 comparison result: {compare_adjacent_numbers(list3)}")
    print(f"List 4 comparison result: {compare_adjacent_numbers(list4)}")
    print(f"List 5 comparison result: {compare_adjacent_numbers(list5)}")
    print(f"List 6 comparison result: {compare_adjacent_numbers(list6)}")