LIST_COMBINATION_METHOD = "list_comprehension"

def combine_lists(list1, list2):
    if LIST_COMBINATION_METHOD == "list_comprehension":
        return [item for sublist in (list1, list2) for item in sublist]
    else:
        raise ValueError("Unsupported combination method")

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    combined_list = combine_lists(sample_list1, sample_list2)
    print(combined_list)