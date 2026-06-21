def filter_valid_weights(weight_list):
    valid_weights = []
    for weight in weight_list:
        try:
            numeric_weight = float(weight)
            if numeric_weight > 0:
                valid_weights.append(numeric_weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ["70.5", "-30", "200", "abc", "150.25", "0", "99.99"]
    print(filter_valid_weights(sample_weights))