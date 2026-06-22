CONVERSION_FACTOR = 0.9144

def yards_to_meters(yards):
    if yards < 0:
        raise ValueError("Input must be non-negative")
    return yards * CONVERSION_FACTOR

if __name__ == '__main__':
    print(f"5 yards to meters: {yards_to_meters(5):.2f}")
    print(f"10 yards to meters: {yards_to_meters(10):.2f}")