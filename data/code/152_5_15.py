def find_common_elements(list_a, list_b):
    return sorted(set(list_a) & set(list_b))

if __name__ == '__main__':
    list_a_sample = [1, 5, 2, 8, 3, 5]
    list_b_sample = [5, 9, 1, 3, 7, 2]
    result = find_common_elements(list_a_sample, list_b_sample)
    print(result)