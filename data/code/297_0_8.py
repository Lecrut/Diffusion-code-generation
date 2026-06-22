def meters_to_kilometers(meters):
    conversion_factor = 0.001
    return meters * conversion_factor
if __name__ == '__main__':
    sample_value = 5000.0
    result = meters_to_kilometers(sample_value)
    print(result)