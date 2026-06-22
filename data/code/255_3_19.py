def find_tuple_with_highest_sum(tuples_list):
    if not tuples_list:
        return None
    max_tuple = max(tuples_list, key=sum)
    return max_tuple

if __name__ == '__main__':
    sample_data1 = (10, 5, 22, 8)
    sample_data2 = (30, 15, 40, 25)
    sample_data3 = (5, 5, 5, 5)

    result = find_tuple_with_highest_sum([sample_data1, sample_data2, sample_data3])
    print(result)