def combine_and_sort(list_a, list_b):
    combined_list = list_a + list_b
    return sorted(combined_list)
if __name__ == '__main__':
    list_a = [5, 2, 8, 1]
    list_b = [9, 3, 4, 6]
    result = combine_and_sort(list_a, list_b)
    print(result)