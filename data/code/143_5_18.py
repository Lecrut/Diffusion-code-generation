def is_contradictory(list1, list2):
    return [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'grape', 'orange']
    print(is_contradictory(sample_list1, sample_list2))