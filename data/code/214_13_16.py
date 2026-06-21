def find_lowest_number(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    smallest = data_list[0]
    for item in data_list[1:]:
        if item < smallest:
            smallest = item
    return smallest

if __name__ == '__main__':
    sample_data_1 = [5, 2, 8, 1, 9]
    sample_data_2 = [-10, 0, 50, -5]
    sample_data_3 = [42]
    sample_data_4 = []

    print(f"Smallest in {sample_data_1}: {find_lowest_number(sample_data_1)}")
    print(f"Smallest in {sample_data_2}: {find_lowest_number(sample_data_2)}")
    print(f"Smallest in {sample_data_3}: {find_lowest_number(sample_data_3)}")