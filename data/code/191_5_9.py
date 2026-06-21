def combine_booleans(list_a, list_b):
    return [a or b for a, b in zip(list_a, list_b)]

if __name__ == '__main__':
    list_a = [True, False, True]
    list_b = [False, True, False]
    combined_list = combine_booleans(list_a, list_b)
    print(combined_list)