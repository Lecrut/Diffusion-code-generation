def compare_lengths(lengths_a, lengths_b):
    for la, lb in zip(lengths_a, lengths_b):
        yield la == lb

if __name__ == '__main__':
    results = list(compare_lengths([1, 2, 3], [1, 2, 4]))
    print(results)