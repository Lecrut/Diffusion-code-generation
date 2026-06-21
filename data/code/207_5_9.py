def find_max_stringified_numbers(numbers):
    max_number = float('-inf')
    for num_str in numbers:
        try:
            num = int(num_str)
            if num > max_number:
                max_number = num
        except ValueError:
            continue
    return max_number

if __name__ == '__main__':
    sample_data1 = ["10", "5", "20", "8", "30"]
    print("Max of sample_data1:", find_max_stringified_numbers(sample_data1))
    
    sample_data2 = ["-5", "-1", "-10", "-2"]
    print("Max of sample_data2:", find_max_stringified_numbers(sample_data2))
    
    sample_data3 = ["42", "7", "37"]
    print("Max of sample_data3:", find_max_stringified_numbers(sample_data3))