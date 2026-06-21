def filter_valid_weights(weight_measurements):
    POSITIVE_THRESHOLD = 0.0
    valid_weights = []
    for weight in weight_measurements:
        try:
            numeric_weight = float(weight)
            if numeric_weight > POSITIVE_THRESHOLD:
                valid_weights.append(numeric_weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ["100.5", "-20", "300", "def", "200.75", "0", "199.99"]
    print(filter_valid_weights(sample_weights))