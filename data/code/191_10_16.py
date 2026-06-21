SAMPLE_LIST_1 = [1, 2, 3]
SAMPLE_LIST_2 = [4, 5, 6]

def combine_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    combined_list = combine_lists(SAMPLE_LIST_1, SAMPLE_LIST_2)
    print(combined_list)