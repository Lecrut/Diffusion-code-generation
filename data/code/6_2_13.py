def weight_differences(weight_pairs):
    for pair in weight_pairs:
        yield pair[0] - pair[1]

if __name__ == '__main__':
    sample_pairs = [(150, 140), (200, 180), (160, 165), (100, 90)]
    for diff in weight_differences(sample_pairs):
        print(diff)