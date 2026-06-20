def find_out_of_range_weights(weights, lower_bound=50, upper_bound=200):
    out_of_range = []
    for weight in weights:
        if weight < lower_bound or weight > upper_bound:
            out_of_range.append(weight)
    return out_of_range

if __name__ == '__main__':
    sample_weights = [45, 60, 150, 210, 199, 50, 200, 10, 100]
    result = find_out_of_range_weights(sample_weights)
    print(result)