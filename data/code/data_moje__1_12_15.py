def filter_valid_weights(weight_measurements):
    valid_weights = []
    for measurement in weight_measurements:
        try:
            weight = float(measurement)
            if weight > 0:
                valid_weights.append(weight)
        except (ValueError, TypeError):
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ['10.5', '20', '-5', 'abc', '0', '30.2', '  ', '15 kg']
    result = filter_valid_weights(sample_weights)
    print(result)