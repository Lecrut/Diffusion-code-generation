def identify_out_of_range_weights(weights, min_limit, max_limit):
    return [weight for weight in weights if weight < min_limit or weight > max_limit]

if __name__ == '__main__':
    sample_weights = [45, 55, 60, 190, 205, 300, 50, 200, 49, 201]
    min_acceptable = 50
    max_acceptable = 200
    out_of_range_results = identify_out_of_range_weights(sample_weights, min_acceptable, max_acceptable)
    print(out_of_range_results)