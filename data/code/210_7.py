def calculate_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum
if __name__ == '__main__':
    list1 = [10, 5.5, 20, 3.14]
    result1 = calculate_range(list1)
    print(f"Range of {list1}: {result1}")
    list2 = [-5, 100, 0.5, -10]
    result2 = calculate_range(list2)
    print(f"Range of {list2}: {result2}")
    list3 = [7]
    result3 = calculate_range(list3)
    print(f"Range of {list3}: {result3}")
    list4 = []
    result4 = calculate_range(list4)
    print(f"Range of {list4}: {result4}")