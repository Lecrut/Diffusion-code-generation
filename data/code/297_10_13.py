METERS_TO_KILOMETERS = 1 / 1000

def meters_to_kilometers(meters):
    if meters < 0:
        raise ValueError("Negative input not allowed.")
    return meters * METERS_TO_KILOMETERS

if __name__ == '__main__':
    sample_values = [1000, 500, 250, -1]
    for value in sample_values:
        try:
            print(f"{value} meters is {meters_to_kilometers(value)} kilometers")
        except ValueError as e:
            print(e)