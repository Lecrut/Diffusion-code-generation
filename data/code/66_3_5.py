def adjacent_pairs_generator(lst):
    for i in range(len(lst) - 1):
        yield (lst[i] < lst[i + 1])
if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7]
    sample_input_2 = [1, 5, 3, 7]
    sample_input_3 = [10, 20, 20, 30]
    sample_input_4 = [5, 5, 5]
    sample_input_5 = [1, 2, 1]
    print(list(adjacent_pairs_generator(sample_input_1)))
    print(list(adjacent_pairs_generator(sample_input_2)))
    print(list(adjacent_pairs_generator(sample_input_3)))
    print(list(adjacent_pairs_generator(sample_input_4)))
    print(list(adjacent_pairs_generator(sample_input_5)))