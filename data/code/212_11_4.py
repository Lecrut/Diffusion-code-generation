def calculate_range(data):
    if not data:
        return 0
    return max(data) - min(data)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(calculate_range(list1))
    list2 = [-10, 0, 5, -5]
    print(calculate_range(list2))
    list3 = [7]
    print(calculate_range(list3))
    list4 = []
    print(calculate_range(list4))