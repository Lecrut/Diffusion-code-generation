def calculate_difference(data):
    if len(data) < 2:
        raise ValueError("List must contain at least two elements to calculate the difference.")
    first = data[0]
    last = data[-1]
    return last - first
if __name__ == '__main__':
    list1 = [1, 5, 10, 15]
    list2 = [3]
    list3 = [100, 200]
    list4 = [5]
    try:
        result1 = calculate_difference(list1)
        print(f"Difference for {list1}: {result1}")
        result3 = calculate_difference(list3)
        print(f"Difference for {list3}: {result3}")
        try:
            calculate_difference(list2)
        except ValueError as e:
            print(f"Error for {list2}: {e}")
        try:
            calculate_difference(list4)
        except ValueError as e:
            print(f"Error for {list4}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")