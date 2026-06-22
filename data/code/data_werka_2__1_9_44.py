def filter_valid_weights(weight_measurements):
    valid_weights = []
    for weight in weight_measurements:
        try:
            numeric_weight = float(weight)
            if numeric_weight > 0:
                valid_weights.append(numeric_weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ["72.5", "-34.0", "180", "invalid", "99.9", "0", "200.1"]
    print(filter_valid_weights(sample_weights))