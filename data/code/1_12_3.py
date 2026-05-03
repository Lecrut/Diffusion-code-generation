def filter_weights(weight_strings):
    valid_weights = []
    for weight_str in weight_strings:
        try:
            weight = float(weight_str)
            if weight > 0:
                valid_weights.append(weight)
        except ValueError:
            continue
    return valid_weights
if __name__ == '__main__':
    sample_weights = ["10.5", "20", "invalid", "-5.2", "0", "33.1"]
    result = filter_weights(sample_weights)
    print(result)