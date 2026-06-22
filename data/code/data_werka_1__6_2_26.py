def weight_difference_generator(weight_pairs):
    for weight1, weight2 in weight_pairs:
        yield abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight_pairs = [(80, 75), (90, 92), (60, 60), (70, 85)]
    for difference in weight_difference_generator(sample_weight_pairs):
        print(difference)