def find_out_of_range_weights(weights, lower_bound=50, upper_bound=200):
    return [weight for weight in weights if weight < lower_bound or weight > upper_bound]

if __name__ == '__main__':
    sample_weights = [45, 60, 205, 150, 30, 200, 50, 250, 100]
    out_of_range = find_out_of_range_weights(sample_weights)
    print(out_of_range)