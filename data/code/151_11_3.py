def combine_lists_extend(list_a, list_b):
    list_a.extend(list_b)
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    combine_lists_extend(list_a, list_b)
    print(list_a)