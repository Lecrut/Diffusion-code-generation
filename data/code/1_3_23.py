def identify_out_of_range_measurements(weights, lower_bound=50, upper_bound=200):
    out_of_range = []
    for weight in weights:
        if not (lower_bound <= weight <= upper_bound):
            out_of_range.append(weight)
    return out_of_range

if __name__ == '__main__':
    sample_weights = [45, 60, 195, 210, 75, 80, 25, 300]
    result = identify_out_of_range_measurements(sample_weights)
    print(result)