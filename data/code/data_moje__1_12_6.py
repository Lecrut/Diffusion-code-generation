def filter_valid_weights(weight_strings):
    valid_weights = []
    for weight in weight_strings:
        try:
            numeric_weight = float(weight)
            if numeric_weight > 0:
                valid_weights.append(numeric_weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ['1.5', '2.3', 'invalid', '-3.0', '0.0', '4.5', '', 'abc', '10']
    result = filter_valid_weights(sample_weights)
    print(result)