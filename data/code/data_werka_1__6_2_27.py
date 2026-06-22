def weight_difference_generator(weight_pairs):
    for weight1, weight2 in weight_pairs:
        yield abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight_pairs = [(70, 65), (80, 78), (90, 92)]
    diff_generator = weight_difference_generator(sample_weight_pairs)
    for diff in diff_generator:
        print(diff)