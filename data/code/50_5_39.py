def non_negative_difference(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    return max(0, abs(a - b))

if __name__ == '__main__':
    sample_values = {'x': 5, 'y': 12}
    print(non_negative_difference(sample_values['x'], sample_values['y']))