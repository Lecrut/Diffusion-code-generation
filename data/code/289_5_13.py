def convert_yards_to_meters(yards):
    if yards < 0:
        raise ValueError("Yards must be non-negative")
    return yards * 0.9144

if __name__ == '__main__':
    print(f"5 yards to meters: {convert_yards_to_meters(5):.2f}")
    print(f"10 yards to meters: {convert_yards_to_meters(10):.2f}")
    print(f"15 yards to meters: {convert_yards_to_meters(15):.2f}")