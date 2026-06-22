def validate_liter_to_gallon(liters):
    if not isinstance(liters, (int, float)) or liters < 0:
        raise ValueError("Invalid input. Liters must be a non-negative number.")

def convert_liter_to_gallon(liters):
    validate_liter_to_gallon(liters)
    return f"{liters} L is {liters * 0.264172:.2f} gallons"

if __name__ == '__main__':
    sample_liters = 5
    print(convert_liter_to_gallon(sample_liters))