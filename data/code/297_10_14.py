def meters_to_kilometers(meters):
    if meters < 0:
        raise ValueError("Negative input not allowed")
    return meters / 1000.0

if __name__ == '__main__':
    sample_values = [-1, 0, 1000, 5000]
    for value in sample_values:
        try:
            print(f"{value} meters is {meters_to_kilometers(value)} kilometers")
        except ValueError as e:
            print(e)