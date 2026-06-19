def adjacent_pairs_generator(input_list):
    try:
        if not all(isinstance(x, (int, float)) for x in input_list):
            raise ValueError("All elements must be numbers.")
        for i in range(len(input_list) - 1):
            yield input_list[i] <= input_list[i + 1]
    except TypeError:
        raise ValueError("Input must be a list of numbers.")

if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7, 9]
    sample_input_2 = [1, 3, 2, 5]
    sample_input_3 = [10, 20, 20, 30]
    sample_input_4 = [5, 5, 5]
    sample_input_5 = [1, 2, 1]

    print(list(adjacent_pairs_generator(sample_input_1)))
    print(list(adjacent_pairs_generator(sample_input_2)))
    print(list(adjacent_pairs_generator(sample_input_3)))
    print(list(adjacent_pairs_generator(sample_input_4)))
    print(list(adjacent_pairs_generator(sample_input_5)))