UNIQUE_SET = set

def combine_unique_lists(list_a, list_b):
    set_a = UNIQUE_SET(list_a)
    set_b = UNIQUE_SET(list_b)
    combined_set = set_a.union(set_b)
    return sorted(combined_set)

if __name__ == '__main__':
    list_a_sample = [1.5, 2.3, 3.7, 4.1]
    list_b_sample = [2.3, 3.7, 4.9, 6.0]
    result = combine_unique_lists(list_a_sample, list_b_sample)
    print(result)