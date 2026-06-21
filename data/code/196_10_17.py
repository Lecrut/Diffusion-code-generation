DEFAULT_LIST_1 = [1, 2, 3]
DEFAULT_LIST_2 = [4, 5, 6]

def concatenate_lists(list1=DEFAULT_LIST_1, list2=DEFAULT_LIST_2):
    result = list1.copy()
    result.extend(list2)
    return result
if __name__ == '__main__':
    combined_list = concatenate_lists()
    print(combined_list)