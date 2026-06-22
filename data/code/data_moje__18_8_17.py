def get_middle_value(numbers):
    length = len(numbers)
    if length == 0:
        return None
    middle_index = length // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_data_even = [10, 20, 30, 40, 50, 60]
    sample_data_odd = [1, 3, 5, 7, 9]
    sample_data_single = [42]
    sample_data_empty = []
    
    result1 = get_middle_value(sample_data_even)
    result2 = get_middle_value(sample_data_odd)
    result3 = get_middle_value(sample_data_single)
    result4 = get_middle_value(sample_data_empty)
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)