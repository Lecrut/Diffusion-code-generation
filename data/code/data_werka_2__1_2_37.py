def identify_out_of_range_measurements(weights, lower_bound=50, upper_bound=200):
    return [weight for weight in weights if weight < lower_bound or weight > upper_bound]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 49, 201, 150]
    out_of_range = identify_out_of_range_measurements(sample_weights)
    print(out_of_range)