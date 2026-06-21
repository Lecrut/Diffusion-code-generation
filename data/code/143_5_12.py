def is_contradictory(list1, list2):
    return any((item1 == 'not ' + item2 or item2 == 'not ' + item1 for item1 in list1 for item2 in list2))
if __name__ == '__main__':
    sample_list1 = ['hot', 'cold']
    sample_list2 = ['not hot', 'warm']
    print(is_contradictory(sample_list1, sample_list2))