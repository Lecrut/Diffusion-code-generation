def convert_miles_to_km(miles):
    if not isinstance(miles, (int, float)):
        raise ValueError("Invalid input type. Please provide a number.")
    return miles * 1.60934

if __name__ == '__main__':
    sample_miles = 5
    try:
        result_km = convert_miles_to_km(sample_miles)
        print(f"{sample_miles} miles is {result_km} kilometers")
    except ValueError as e:
        print(e)