def average_pairs(nested_tuples):
    return [sum(pair) / 2 for pair in nested_tuples]

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5, 6))
    print(average_pairs(sample_data))