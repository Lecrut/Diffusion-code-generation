def adjacent_pairs_generator(lst):
    for i in range(len(lst) - 1):
        yield lst[i] < lst[i + 1]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [5, 4, 3, 2, 1]
    sample_list_3 = [1, 3, 2, 4, 5]
    sample_list_4 = [10, 20, 30, 40, 50]
    sample_list_5 = [1, 1, 1, 1, 1]

    print(list(adjacent_pairs_generator(sample_list_1)))
    print(list(adjacent_pairs_generator(sample_list_2)))
    print(list(adjacent_pairs_generator(sample_list_3)))
    print(list(adjacent_pairs_generator(sample_list_4)))
    print(list(adjacent_pairs_generator(sample_list_5)))