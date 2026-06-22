def validate_yard(value):
    if value < 0:
        raise ValueError("Yard value must be non-negative")

def yards_to_kilometers(yards):
    validate_yard(yards)
    return yards * 0.0009144

if __name__ == '__main__':
    sample_yards = 1000
    result_km = yards_to_kilometers(sample_yards)
    print(result_km)