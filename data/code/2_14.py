LITER_TO_MILLILITER = 1000.0
GALLON_TO_MILLILITER = 3785.411784
CUBIC_INCH_TO_MILLILITER = 16.387064

def convert_to_milliliters(volumes):
    converted = []
    for value, unit in volumes:
        if value < 0:
            converted.append(0.0)
        elif value == 0:
            converted.append(0.0)
        else:
            if unit == "liters":
                converted.append(value * LITER_TO_MILLILITER)
            elif unit == "gallons":
                converted.append(value * GALLON_TO_MILLILITER)
            elif unit == "cubic_inches":
                converted.append(value * CUBIC_INCH_TO_MILLILITER)
            else:
                converted.append(0.0)
    return converted

if __name__ == '__main__':
    sample_volumes = [
        (1.0, "liters"),
        (0.5, "gallons"),
        (10.0, "cubic_inches"),
        (0.0, "liters"),
        (-5.0, "gallons"),
        (2.5, "cubic_inches")
    ]
    result = convert_to_milliliters(sample_volumes)
    print(result)