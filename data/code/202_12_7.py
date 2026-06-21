def find_largest_number(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    
    try:
        max_value = float(data_list[0])
        for item in data_list[1:]:
            number = float(item)
            if number > max_value:
                max_value = number
        return max_value
    except ValueError as e:
        raise ValueError(f"Invalid number found: {e}")

if __name__ == '__main__':
    sample_data1 = [10, 5.5, 20, '8', 15.3]
    sample_data2 = [-5, -1, '-10', -3]
    sample_data3 = [42.75, 42.25, 42.5]

    print(f"Largest number in {sample_data1}: {find_largest_number(sample_data1)}")
    print(f"Largest number in {sample_data2}: {find_largest_number(sample_data2)}")
    print(f"Largest number in {sample_data3}: {find_largest_number(sample_data3)}")