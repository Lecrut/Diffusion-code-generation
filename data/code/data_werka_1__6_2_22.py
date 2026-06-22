def weight_difference_generator(weight_pairs):
    for pair in weight_pairs:
        yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    sample_weight_pairs = [(70, 65), (80, 85), (90, 88)]
    differences = weight_difference_generator(sample_weight_pairs)
    for diff in differences:
        print(diff)