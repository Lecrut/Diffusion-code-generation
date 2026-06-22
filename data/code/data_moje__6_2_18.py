def weight_difference_generator(pairs):
    for first, second in pairs:
        yield abs(first - second)

if __name__ == '__main__':
    sample_pairs = [(100, 95), (200, 210), (50, 50), (150, 140)]
    for diff in weight_difference_generator(sample_pairs):
        print(diff)