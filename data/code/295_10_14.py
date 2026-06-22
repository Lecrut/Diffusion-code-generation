CONVERSION_FACTOR = 0.621371

def kilometers_to_miles(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Kilometers must be a numeric value.")
    return kilometers * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kilometers = 10.0
    try:
        result_miles = kilometers_to_miles(sample_kilometers)
        print(f"{sample_kilometers} kilometers is equal to {result_miles} miles.")
    except ValueError as e:
        print(e)