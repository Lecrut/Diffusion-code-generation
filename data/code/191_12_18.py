import itertools

def combine_lists(list1, list2):
    return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    LIST_A = [1, 2, 3]
    LIST_B = ['a', 'b', 'c']
    combined_list = combine_lists(LIST_A, LIST_B)
    print(combined_list)