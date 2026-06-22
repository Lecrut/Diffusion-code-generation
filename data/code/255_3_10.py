def find_tuple_with_max_sum(tuples_list):
    if not tuples_list:
        return None
    
    max_sum = float('-inf')
    result_tuple = ()
    
    for current_tuple in tuples_list:
        current_sum = sum(current_tuple)
        if current_sum > max_sum:
            max_sum = current_sum
            result_tuple = current_tuple
            
    return result_tuple

if __name__ == '__main__':
    sample_data1 = (10, 5, 22, 8)
    sample_data2 = (30, 15, 40, 25)
    sample_data3 = (2, 3, 7)
    
    tuples_list = [sample_data1, sample_data2, sample_data3]
    max_tuple = find_tuple_with_max_sum(tuples_list)
    print(max_tuple)