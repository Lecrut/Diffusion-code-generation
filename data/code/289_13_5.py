conversion_factor = 0.9144

def validate_yards(yards):
    if not all(isinstance(y, (int, float)) and y >= 0 for y in yards):
        raise ValueError("All yard values must be non-negative numbers")

def yards_to_meters(yards):
    validate_yards(yards)
    return [round(y * conversion_factor, 3) for y in yards]

if __name__ == '__main__':
    sample_yards = [10, 20, 30]
    print(yards_to_meters(sample_yards))