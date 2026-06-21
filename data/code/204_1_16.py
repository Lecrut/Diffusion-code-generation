def validate_data(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Data must be a non-empty list")

def find_middle_value(data):
    validate_data(data)
    n = len(data)
    middle_index = n // 2
    return data[middle_index] if n % 2 == 1 else (data[middle_index - 1] + data[middle_index]) / 2

if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [1, 5, 3, 4, 2]
    list3 = [10, 20, 30, 40]
    list4 = [7, 8, 9, 10]
    list5 = [1, 2, 3, 4, 5, 6]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    print(f"Median of {list2}: {find_middle_value(list2)}")
    print(f"Median of {list3}: {find_middle_value(list3)}")
    print(f"Median of {list4}: {find_middle_value(list4)}")
    print(f"Median of {list5}: {find_middle_value(list5)}")