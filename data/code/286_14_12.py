def yards_to_meters(yards):
    if not isinstance(yards, (int, float)) or yards < 0:
        raise ValueError("Invalid input: Yards must be a non-negative number")
    return yards * 0.9144

if __name__ == '__main__':
    yard_values = [1.0, 5.0, 10.5, 100.0]
    for yard in yard_values:
        meters = yards_to_meters(yard)
        print(f"{yard} yards is equal to {meters} meters")