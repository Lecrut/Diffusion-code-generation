def yards_to_meters(yards):
    conversion_factor = 0.9144
    return [y * conversion_factor for y in yards]

if __name__ == '__main__':
    sample_values = [1.0, 5.0, 10.5, 100.0]
    meters_values = yards_to_meters(sample_values)
    print(meters_values)