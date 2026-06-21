def count_diff_case_insensitive(list1, list2):
    from collections import Counter
    counter1 = Counter((word.lower() for word in list1))
    counter2 = Counter((word.lower() for word in list2))
    diff_counter = counter1 - counter2
    return dict(diff_counter)
if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry', 'apple']
    sample_list2 = ['banana', 'cherry', 'grape']
    result = count_diff_case_insensitive(sample_list1, sample_list2)
    print(result)