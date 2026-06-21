def combine_lists(list1, list2):
    return list(zip(list1, list2))

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    combined_result = combine_lists(list_a, list_b)
    print(f"Combined list of {list_a} and {list_b}: {combined_result}")