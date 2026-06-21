def find_largest_number(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    
    max_value = float('-inf')
    for number in data_list:
        try:
            num_float = float(number)
            if num_float > max_value:
                max_value = num_float
        except ValueError:
            continue
    
    return max_value

if __name__ == '__main__':
    sample_data1 = [10, 5.5, "20", 8, 15]
    sample_data2 = [-5, -1, "-10", -3]
    sample_data3 = ["42"]
    sample_data4 = []
    
    print(f"Maximum of {sample_data1}: {find_largest_number(sample_data1)}")
    print(f"Maximum of {sample_data2}: {find_largest_number(sample_data2)}")
    print(f"Maximum of {sample_data3}: {find_largest_number(sample_data3)}")
    try:
        print(f"Maximum of {sample_data4}: {find_largest_number(sample_data4)}")
    except ValueError as e:
        print(e)