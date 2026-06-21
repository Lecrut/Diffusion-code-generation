from itertools import chain

def concatenate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list(chain(list1, list2))

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result_list = concatenate_lists(list_a, list_b)
    print(result_list)