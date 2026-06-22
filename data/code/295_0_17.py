def meters_to_kilometers(meters):
    if not isinstance(meters, (int, float)) or meters < 0:
        raise ValueError("Input must be a non-negative number")
    return round(meters / 1000.0, 2)

if __name__ == '__main__':
    meters_value = 1500
    kilometers_value = meters_to_kilometers(meters_value)
    print(f"{meters_value} meters is equal to {kilometers_value} kilometers")