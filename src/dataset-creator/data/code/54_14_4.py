def find_middle_index(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    n = len(data)
    middle_position = (n // 2) - 1
    return data[middle_position]
if __name__ == '__main__':
    sample_list = [50, 49, 38, 67, 76, 83, 89, 87]
    try:
        middle_value = find_middle_index(sample_list)
        print(f"Middle value at index {sample_list.index(middle_value)} is:", middle_value)
    except IndexError as e:
        if sample_list and len(sample_list) == 0:
            raise ValueError("List cannot be empty.") from e