GALLONS_TO_LITERS_FACTOR = 3.78541

def validate_input(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Input must be a non-negative number")

def gallons_to_liters(gallons):
    validate_input(gallons)
    return gallons * GALLONS_TO_LITERS_FACTOR

LITERS_TO_GALLONS_FACTOR = 1 / GALLONS_TO_LITERS_FACTOR

def liters_to_gallons(liters):
    validate_input(liters)
    return liters * LITERS_TO_GALLONS_FACTOR

if __name__ == '__main__':
    print(gallons_to_liters(1))
    print(liters_to_gallons(1))