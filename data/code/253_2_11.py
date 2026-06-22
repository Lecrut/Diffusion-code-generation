def find_the_middle_value_among_three_batch_process(values):
    return [sorted(triplet)[1] for triplet in values]

if __name__ == '__main__':
    sample_values = [
        (1, 5, 3),
        (10, 20, 5),
        (7, 1, 9),
        (4, 8, 2),
        (100, 50, 25)
    ]
    print(find_the_middle_value_among_three_batch_process(sample_values))