import itertools

def concatenate_lists(list1, list2):
    return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    LIST_A = [1, 2, 3]
    LIST_B = ['a', 'b', 'c']
    result_list = concatenate_lists(LIST_A, LIST_B)
    print(result_list)