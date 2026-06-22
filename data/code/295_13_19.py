GALLONS_TO_LITERS_FACTOR = 3.78541

def validate_volume(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Volume must be a non-negative number")

def gallons_to_liters(gallons):
    validate_volume(gallons)
    return gallons * GALLONS_TO_LITERS_FACTOR

def liters_to_gallons(liters):
    validate_volume(liters)
    return liters / GALLONS_TO_LITERS_FACTOR

if __name__ == '__main__':
    print(gallons_to_liters(1))
    print(liters_to_gallons(1))