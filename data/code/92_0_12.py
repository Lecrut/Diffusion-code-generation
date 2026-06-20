def opposite_truth(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        try:
            result = opposite_truth(val)
            print(result)
        except ValueError as e:
            print(e)