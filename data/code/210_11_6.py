def calculate_data_range(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    return max(data) - min(data)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 4, 15, 2]
    empty_list = []
    list3 = [7]
    print(f"Range of {list1}: {calculate_data_range(list1)}")
    print(f"Range of {list2}: {calculate_data_range(list2)}")
    try:
        print(f"Range of {empty_list}: {calculate_data_range(empty_list)}")
    except ValueError as e:
        print(f"Error for {empty_list}: {e}")
    print(f"Range of {list3}: {calculate_data_range(list3)}")