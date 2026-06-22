def filter_valid_weights(weight_strings):
    valid_weights = []
    for s in weight_strings:
        try:
            value = float(s)
            if value > 0:
                valid_weights.append(value)
        except (ValueError, TypeError):
            continue
    return valid_weights

if __name__ == '__main__':
    sample_data = ["10.5", "-3.2", "abc", "0", "25", "12.3kg", "45.67", "", "50"]
    result = filter_valid_weights(sample_data)
    print(result)