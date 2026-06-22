def validate_volume(value):
    if value < 0:
        raise ValueError("Volume cannot be negative.")

def gallons_to_liters(gallons):
    validate_volume(gallons)
    return gallons * 3.78541

def liters_to_gallons(liters):
    validate_volume(liters)
    return liters / 3.78541

if __name__ == '__main__':
    print(gallons_to_liters(1))
    print(liters_to_gallons(1))