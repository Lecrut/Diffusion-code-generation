def filter_valid_weights(weight_measurements):
    valid_weights = []
    for weight in weight_measurements:
        try:
            value = float(weight)
            if value > 0:
                valid_weights.append(value)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_data = ["10.5", "-3.2", "abc", "0", "25.0", " 15 ", "invalid", "7.75", "0.001"]
    result = filter_valid_weights(sample_data)
    print(result)