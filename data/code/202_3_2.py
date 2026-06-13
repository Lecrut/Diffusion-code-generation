def calculate_max(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    return max(data)
if __name__ == '__main__':
    list1 = [1, 5, 2, 9, 3]
    list2 = [-10, -5, -20]
    list3 = []
    try:
        result1 = calculate_max(list1)
        print(f"Max of {list1}: {result1}")
        result2 = calculate_max(list2)
        print(f"Max of {list2}: {result2}")
        calculate_max(list3)
    except ValueError as e:
        print(f"Error caught: {e}")