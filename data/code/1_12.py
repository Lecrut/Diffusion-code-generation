def filter_valid_weights(weight_strings):
    valid_weights = []
    for item in weight_strings:
        try:
            value = float(item)
            if value > 0:
                valid_weights.append(value)
        except (ValueError, TypeError):
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ['10.5', '5.0', '-3.2', 'invalid', '0', '7.8', '', 'abc', '12']
    result = filter_valid_weights(sample_weights)
    print(result)