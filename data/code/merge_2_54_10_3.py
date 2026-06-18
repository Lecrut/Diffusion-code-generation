def find_middle_position(data):
    if not data:
        return None
    length = len(data)
    if length % 2 == 1:
        middle_index = (length - 1) // 2
        return middle_index, [data[middle_index]]
    else:
        left_middle = (length // 2) - 1
        right_middle = (length // 2)
        return f"{left_middle}, {right_middle}", data[left_middle], data[right_middle]
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    result_single = find_middle_position(sample_list_1)
    print(f"Odd length list: {result_single}")
    empty_result = find_middle_position([])
    print(f"Empty list: {empty_result}")
    sample_list_2 = [1, 2, 3]
    result_pair = find_middle_position(sample_list_2)
    print(f"Even length list: {result_pair}")