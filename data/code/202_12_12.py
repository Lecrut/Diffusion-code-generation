def find_largest_number(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    
    max_value = float('-inf')
    for item in data_list:
        try:
            num = float(item)
            if num > max_value:
                max_value = num
        except ValueError:
            continue
    
    return max_value

if __name__ == '__main__':
    sample_data1 = [10, 5.5, '20', -8, 15]
    sample_data2 = [-5, -1.1, '-10', -3]
    sample_data3 = ['42']
    sample_data4 = []
    
    try:
        result1 = find_largest_number(sample_data1)
        print(f"Maximum of {sample_data1}: {result1}")
        
        result2 = find_largest_number(sample_data2)
        print(f"Maximum of {sample_data2}: {result2}")
        
        result3 = find_largest_number(sample_data3)
        print(f"Maximum of {sample_data3}: {result3}")
        
        find_largest_number(sample_data4)
    except ValueError as e:
        print(e)