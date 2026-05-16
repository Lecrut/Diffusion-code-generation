def combine_lists_extend(list_a, list_b):
    list_a.extend(list_b)
if __name__ == '__main__':
    list_a_sample = [1, 2, 3]
    list_b_sample = [4, 5, 6]
    combine_lists_extend(list_a_sample, list_b_sample)
    print(list_a_sample)