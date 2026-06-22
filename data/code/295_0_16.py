def meters_to_kilometers(meters):
    return meters / 1000.0

if __name__ == '__main__':
    meters_value = 5000.0
    kilometers_value = meters_to_kilometers(meters_value)
    print(f"{meters_value} meters is equal to {kilometers_value:.2f} kilometers")