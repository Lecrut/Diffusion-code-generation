def convert_kilometers_to_miles(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number.")
    return round(kilometers * 0.621371, 2)

if __name__ == '__main__':
    sample_km = 100
    try:
        result_miles = convert_kilometers_to_miles(sample_km)
        print(f"{sample_km} kilometers is equal to {result_miles:.2f} miles.")
    except ValueError as e:
        print(f"Error: Invalid input provided. Details: {e}", file=sys.stderr)