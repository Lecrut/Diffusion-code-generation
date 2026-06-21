LIST_A = [1, 2, 3]
LIST_B = [4, 5, 6]

def concatenate_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result
if __name__ == '__main__':
    final_result = concatenate_lists(LIST_A, LIST_B)
    print(final_result)