def filter_valid_weights(weights):
    valid_weights = []
    for w in weights:
        try:
            value = float(w)
            if value > 0:
                valid_weights.append(value)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ['10.5', '-3.2', '0', '25', 'abc', '7.8', '', '  5  ', '-0.1', '100']
    result = filter_valid_weights(sample_weights)
    print(result)