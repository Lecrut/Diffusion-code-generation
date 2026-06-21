def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [40, 50, 60]
    combined_list = concatenate_lists(sample_list1, sample_list2)
    print(f"List 1: {sample_list1}")
    print(f"List 2: {sample_list2}")
    print(f"Combined List (using direct concatenation): {combined_list}")