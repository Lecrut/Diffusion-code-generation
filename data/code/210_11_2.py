def calculate_data_range(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    return max(data) - min(data)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 20, 5, 15]
    empty_list = []
    try:
        range1 = calculate_data_range(list1)
        print(f"Data: {list1}, Range: {range1}")
        range2 = calculate_data_range(list2)
        print(f"Data: {list2}, Range: {range2}")
        calculate_data_range(empty_list)
    except ValueError as e:
        print(f"Error caught: {e}")