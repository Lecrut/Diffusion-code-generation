def is_valid_positive_weight(weight_str):
    try:
        weight = float(weight_str)
        return weight > 0
    except ValueError:
        return False

def filter_valid_weights(weight_measurements):
    valid_weights = [weight for weight in weight_measurements if is_valid_positive_weight(weight)]
    return valid_weights

if __name__ == '__main__':
    sample_weights = ["65.4", "-20", "180", "xyz", "90.3", "0", "88.88"]
    print(filter_valid_weights(sample_weights))