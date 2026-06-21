def create_lookup_table(list1, list2):
    return dict(zip(list1, list2))

if __name__ == '__main__':
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    lookup_table = create_lookup_table(keys, values)
    print(lookup_table)