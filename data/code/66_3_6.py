def adjacent_pair_generator(lst):
    try:
        if not all(isinstance(x, (int, float)) for x in lst):
            raise ValueError("All elements must be numbers")
        if len(lst) < 2:
            return
        for i in range(len(lst) - 1):
            yield lst[i] <= lst[i + 1]
    except TypeError:
        raise ValueError("Input must be a list of numbers")

if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7]
    sample_input_2 = [10, 20, 20, 30]
    sample_input_3 = [5, 5, 5]
    sample_input_4 = [1, 2, 1]

    print(list(adjacent_pair_generator(sample_input_1)))
    print(list(adjacent_pair_generator(sample_input_2)))
    print(list(adjacent_pair_generator(sample_input_3)))
    print(list(adjacent_pair_generator(sample_input_4)))