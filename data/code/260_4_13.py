def find_common_reversed(list1, list2):
    return [item for item in set(list1) & set(list2)][::-1]

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    print(find_common_reversed(sample_list1, sample_list2))