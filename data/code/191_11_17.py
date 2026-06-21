def merge_lists(list_a, list_b):
    return [*list_a, *list_b]

if __name__ == '__main__':
    sample_list_a = [10, 20, 30]
    sample_list_b = [40, 50, 60]
    merged_result = merge_lists(sample_list_a, sample_list_b)
    print(merged_result)