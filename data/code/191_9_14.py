def join_lists(list_one, list_two):
    combined_list = list_one + list_two
    return combined_list

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [40, 50, 60, 70]
    result = join_lists(sample_list1, sample_list2)
    print(result)
    
    sample_list3 = ['red', 'green', 'blue']
    sample_list4 = ['green', 'yellow', 'purple']
    result2 = join_lists(sample_list3, sample_list4)
    print(result2)