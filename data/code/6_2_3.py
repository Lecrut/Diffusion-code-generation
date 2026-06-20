def weight_difference_generator(pairs):
    for left, right in pairs:
        yield left - right

if __name__ == '__main__':
    sample_pairs = [(10, 5), (20, 15), (8, 12)]
    for diff in weight_difference_generator(sample_pairs):
        print(diff)