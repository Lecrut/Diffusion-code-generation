def extract_valid_weights(measurements):
    valid_weights = []
    for measurement in measurements:
        try:
            weight = float(measurement)
            if weight > 0:
                valid_weights.append(weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_data = ["10.5", "0", "-3.2", "valid", "25.0", "7", "abc", "0.1"]
    result = extract_valid_weights(sample_data)
    print(result)