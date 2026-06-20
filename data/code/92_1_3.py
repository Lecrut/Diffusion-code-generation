def find_opposite_truth(truth):
    if not isinstance(truth, bool):
        raise ValueError("Input must be a boolean value")
    return not truth

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        try:
            result = find_opposite_truth(value)
            print(f"Opposite of {value} is {result}")
        except ValueError as e:
            print(e)