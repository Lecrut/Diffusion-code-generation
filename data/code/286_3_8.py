def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def convert_miles_to_kilometers(miles):
    if not is_valid_number(miles):
        raise TypeError("Invalid input type. Please provide a numeric value.")
    
    return miles * 1.60934

if __name__ == '__main__':
    try:
        result = convert_miles_to_kilometers(5)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)