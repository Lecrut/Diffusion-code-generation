def find_middle_value(data):
    n = len(data)
    if n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (data[lower_middle_index] + data[upper_middle_index]) / 2.0
        return median

if __name__ == '__main__':
    sample_list1 = [5, 3, 7, 1, 4]
    sample_list2 = [8, 6, 7, 5, 3, 0, 9]
    
    print(f"Median of {sample_list1}: {find_middle_value(sample_list1)}")
    print(f"Median of {sample_list2}: {find_middle_value(sample_list2)}")