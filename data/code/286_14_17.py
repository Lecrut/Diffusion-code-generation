def yards_to_meters(yards):
    if not isinstance(yards, (int, float)) or yards < 0:
        raise ValueError("Input must be a non-negative number")
    return yards * 0.9144

if __name__ == '__main__':
    sample_yards = 5
    meters = yards_to_meters(sample_yards)
    print(meters)