def combine_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    LIST_A = ["apple", "banana"]
    LIST_B = ["cherry", "date"]
    combined_list = combine_lists(LIST_A, LIST_B)
    print(combined_list)