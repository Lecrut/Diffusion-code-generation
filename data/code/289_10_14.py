def convert_kilometers_to_miles(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Invalid input type. Please provide a number.")
    
    miles = kilometers * 0.621371
    return round(miles, 2)

if __name__ == '__main__':
    sample_kilometers = 100
    try:
        result_miles = convert_kilometers_to_miles(sample_kilometers)
        print(f"{sample_kilometers} kilometers is equal to {result_miles:.2f} miles.")
    except ValueError as e:
        print(f"Error: Invalid input provided. Details: {e}", file=sys.stderr)