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
    sample_inputs = ['10.5', '-3.2', '0', 'abc', '25', '', '7.89', '  4.5  ']
    result = filter_valid_weights(sample_inputs)
    print(result)