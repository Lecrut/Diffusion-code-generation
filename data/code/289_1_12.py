def miles_to_cm(miles):
    try:
        cm = miles * 160934
        return cm
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_miles = 5
    result = miles_to_cm(sample_miles)
    if result is not None:
        print(f"{sample_miles} miles is {result} centimeters")