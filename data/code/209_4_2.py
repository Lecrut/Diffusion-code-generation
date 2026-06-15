def calculate_average(data):
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
        else:
            raise TypeError("Input contains non-numeric data")
    if not data:
        return 0
    return total / len(data)
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5.5, 10.5, 15.5]
    list3 = [1, 2, "three", 4]
    list4 = []
    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    try:
        calculate_average(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")
    print(f"Average of {list4}: {calculate_average(list4)}")