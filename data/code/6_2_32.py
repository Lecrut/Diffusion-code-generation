def weight_difference_generator(weight_pairs):
    for weight1, weight2 in weight_pairs:
        yield abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weights = [(80, 75), (90, 95), (60, 60)]
    differences = weight_difference_generator(sample_weights)
    for diff in differences:
        print(diff)