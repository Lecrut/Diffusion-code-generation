def create_lookup_table(list1, list2):
    return dict(zip(list1, list2))

if __name__ == '__main__':
    sample_list1 = ['a', 'b', 'c']
    sample_list2 = [1, 2, 3]
    lookup_table = create_lookup_table(sample_list1, sample_list2)
    print(lookup_table)