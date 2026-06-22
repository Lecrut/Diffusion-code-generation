def validate_input(cubic_meters):
    if not isinstance(cubic_meters, (int, float)) or cubic_meters < 0:
        raise ValueError("Invalid input. Please provide a non-negative number in cubic meters.")

def cubic_meters_to_gallons(cubic_meters):
    validate_input(cubic_meters)
    return cubic_meters * 264.172

if __name__ == '__main__':
    print(cubic_meters_to_gallons(1))
    print(cubic_meters_to_gallons(2))