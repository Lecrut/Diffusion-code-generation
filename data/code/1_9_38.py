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
    sample_weights = ["75.5", "-30", "120", "abc", "45.2", "0", "99.9"]
    print(filter_valid_weights(sample_weights))