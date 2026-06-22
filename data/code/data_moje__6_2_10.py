def weight_difference_generator(weight_pairs):
    for first, second in weight_pairs:
        yield first - second

if __name__ == '__main__':
    sample_pairs = [(100, 95), (200, 210), (50, 50), (150, 145)]
    for diff in weight_difference_generator(sample_pairs):
        print(diff)