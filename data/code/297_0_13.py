def meters_to_kilometers(meters):
    conversion_factor = 0.001
    return meters * conversion_factor

if __name__ == '__main__':
    sample_meters = 5000
    print(meters_to_kilometers(sample_meters))