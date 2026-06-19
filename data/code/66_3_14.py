def adjacent_pairs_generator(lst):
    for i in range(len(lst) - 1):
        yield lst[i] < lst[i + 1]

if __name__ == '__main__':
    sample_input = [1, 3, 5, 7, 9]
    result = list(adjacent_pairs_generator(sample_input))
    print(result)
    
    sample_input_2 = [1, 5, 3, 7]
    result_2 = list(adjacent_pairs_generator(sample_input_2))
    print(result_2)

    sample_input_3 = [10, 20, 20, 30]
    result_3 = list(adjacent_pairs_generator(sample_input_3))
    print(result_3)

    sample_input_4 = [5, 5, 5]
    result_4 = list(adjacent_pairs_generator(sample_input_4))
    print(result_4)

    sample_input_5 = [1, 2, 1]
    result_5 = list(adjacent_pairs_generator(sample_input_5))
    print(result_5)