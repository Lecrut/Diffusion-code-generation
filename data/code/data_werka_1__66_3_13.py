def adjacent_pairs_generator(input_list):
    for i in range(len(input_list) - 1):
        yield input_list[i] < input_list[i + 1]

if __name__ == '__main__':
    sample_values = [1, 3, 2, 4, 5]
    result = list(adjacent_pairs_generator(sample_values))
    print(result)