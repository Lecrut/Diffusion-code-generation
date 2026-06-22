def filter_valid_weights(weight_strings):
    valid_weights = []
    for w in weight_strings:
        try:
            value = float(w)
            if value > 0:
                valid_weights.append(value)
        except ValueError:
            continue
    return valid_weights

if __name__ == '__main__':
    sample_weights = ['10.5', 'abc', '-3.2', '0', '7.8', '5', 'xyz', '100']
    result = filter_valid_weights(sample_weights)
    print(result)