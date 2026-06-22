def meters_to_kilometers(meters):
    return round(meters / 1000, 2)

if __name__ == '__main__':
    sample_meters = 500.0
    kilometers_value = meters_to_kilometers(sample_meters)
    print(f"{sample_meters} meters is equal to {kilometers_value} kilometers")