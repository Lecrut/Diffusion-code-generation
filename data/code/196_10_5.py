list1 = [1, 2, 3]
list2 = [4, 5, 6]

def concatenate_lists(list_a, list_b):
    result_list = list_a.copy()
    result_list.extend(list_b)
    return result_list

if __name__ == '__main__':
    concatenated_list = concatenate_lists(list1, list2)
    print(concatenated_list)