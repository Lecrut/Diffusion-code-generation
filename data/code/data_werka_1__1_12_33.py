def filter_valid_weights(weight_list):
    valid_weights = []
    for weight_str in weight_list:
        try:
            weight = float(weight_str)
            if weight > 0:
                valid_weights.append(weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ["70.5", "-23", "45", "invalid", "99.99", "0", "123.45"]
    print(filter_valid_weights(sample_weights))