def filter_valid_weights(weight_list):
    valid_weights = []
    for weight in weight_list:
        try:
            num_weight = float(weight)
            if num_weight > 0:
                valid_weights.append(num_weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ["70.5", "-30", "200", "invalid", "150.25", "0", "99.99"]
    print(filter_valid_weights(sample_weights))