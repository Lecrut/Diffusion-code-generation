MILES_TO_CM = 160934

def convert_miles_to_cm(miles):
    try:
        return miles * MILES_TO_CM
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_distance = 5.0
    result = convert_miles_to_cm(sample_distance)
    if result is not None:
        print(result)