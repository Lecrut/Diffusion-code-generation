def weight_difference_generator(weight_pairs):
    for i in range(len(weight_pairs) - 1):
        yield weight_pairs[i+1] - weight_pairs[i]
if __name__ == '__main__':
    sample_weights = [10, 15, 22, 30, 35]
    differences = weight_difference_generator(sample_weights)
    print(list(differences))