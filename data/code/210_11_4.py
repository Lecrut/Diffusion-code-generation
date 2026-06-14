def calculate_data_range(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    return max(data) - min(data)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 2, 5, 1]
    empty_list = []
    list3 = [42]
    print(f"Data Range for {list1}: {calculate_data_range(list1)}")
    print(f"Data Range for {list2}: {calculate_data_range(list2)}")
    print(f"Data Range for {empty_list}: Error raised")
    print(f"Data Range for {list3}: {calculate_data_range(list3)}")