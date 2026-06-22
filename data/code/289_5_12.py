conversion_factors = {
    'yd': 0.9144,
}

def convert_yards_to_meters(yards):
    if yards < 0:
        raise ValueError("Input must be non-negative")
    return yards * conversion_factors['yd']

if __name__ == '__main__':
    print(f"5 yd to m: {convert_yards_to_meters(5):.2f}")
    print(f"10 yd to m: {convert_yards_to_meters(10):.2f}")
    print(f"15 yd to m: {convert_yards_to_meters(15):.2f}")