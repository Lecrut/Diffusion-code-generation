def calculate_difference(data):
    if len(data) < 2:
        raise ValueError("List must contain at least two elements to calculate the difference.")
    return data[-1] - data[0]
if __name__ == '__main__':
    list1 = [1, 5, 3, 9]
    list2 = [10]
    list3 = [42]
    list4 = [5, 1, 8, 3]
    try:
        result1 = calculate_difference(list1)
        print(f"Difference for {list1}: {result1}")
    except ValueError as e:
        print(f"Error for {list1}: {e}")
    try:
        result2 = calculate_difference(list2)
        print(f"Difference for {list2}: {result2}")
    except ValueError as e:
        print(f"Error for {list2}: {e}")
    try:
        result3 = calculate_difference(list3)
        print(f"Difference for {list3}: {result3}")
    except ValueError as e:
        print(f"Error for {list3}: {e}")
    try:
        result4 = calculate_difference(list4)
        print(f"Difference for {list4}: {result4}")
    except ValueError as e:
        print(f"Error for {list4}: {e}")