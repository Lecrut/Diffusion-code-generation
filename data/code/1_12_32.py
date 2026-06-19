def filter_positive_weights(weight_list):
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
    sample_weights = ["70.5", "-23", "45", "abc", "100.2", "0", "33.3"]
    filtered_weights = filter_positive_weights(sample_weights)
    print(filtered_weights)