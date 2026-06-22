def yards_to_meters(yards):
    if yards < 0:
        raise ValueError("Yards must be non-negative")
    return yards * 0.9144

if __name__ == '__main__':
    print(yards_to_meters(5))
    print(yards_to_meters(10))