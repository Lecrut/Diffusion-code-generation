def is_valid_positive_weight(weight_str):
    try:
        weight = float(weight_str)
        return weight > 0
    except ValueError:
        return False

def filter_valid_weights(weight_measurements):
    valid_weights = []
    for weight in weight_measurements:
        if is_valid_positive_weight(weight):
            valid_weights.append(float(weight))
    return valid_weights

if __name__ == '__main__':
    sample_weights = ["75.5", "-30", "200", "abc", "150.25", "0", "99.99"]
    print(filter_valid_weights(sample_weights))