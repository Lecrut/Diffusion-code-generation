def convert_miles_to_kilometers(miles):
    if not isinstance(miles, (int, float)) or miles < 0:
        raise ValueError("Invalid input: Miles must be a non-negative number")
    return miles * 1.60934

if __name__ == '__main__':
    sample_miles = 5
    try:
        kilometers = convert_miles_to_kilometers(sample_miles)
        print(f"{sample_miles} miles is equal to {kilometers:.2f} kilometers")
    except ValueError as e:
        print(e)