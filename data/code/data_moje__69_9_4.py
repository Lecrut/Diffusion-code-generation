def miles_to_feet(measurements):
    return {key: value * 5280 for key, value in measurements.items()}

if __name__ == '__main__':
    sample_miles = {
        "distance1": 1.5,
        "distance2": 2.0,
        "distance3": 0.75
    }
    result = miles_to_feet(sample_miles)
    print(result)