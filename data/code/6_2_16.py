def weight_difference_generator(pairs):
    for pair in pairs:
        yield pair[0] - pair[1]

if __name__ == '__main__':
    sample_pairs = [(100, 90), (200, 150), (50, 60)]
    result = list(weight_difference_generator(sample_pairs))
    print(result)