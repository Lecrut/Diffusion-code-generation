def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [100, 200, 300]
    sample_list2 = [400, 500, 600]
    combined_list = concatenate_lists(sample_list1, sample_list2)
    print(f"Combined List: {combined_list}")