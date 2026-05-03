import math
def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "liters":
        if to_unit == "milliliters":
            return value * 1000
        elif to_unit == "cubic meters":
            return value * 1000
        elif to_unit == "gallons":
            return value * 0.264172
        elif to_unit == "cubic inches":
            return value * 61023.74
    elif from_unit == "milliliters":
        if to_unit == "liters":
            return value / 1000
        elif to_unit == "cubic meters":
            return value / 1000000
        elif to_unit == "gallons":
            return value * 0.00378541
        elif to_unit == "cubic inches":
            return value * 0.00006102374
    elif from_unit == "cubic meters":
        if to_unit == "liters":
            return value * 1000
        elif to_unit == "milliliters":
            return value * 1000
        elif to_unit == "gallons":
            return value / 0.00378541
        elif to_unit == "cubic inches":
            return value * 163870.673
    elif from_unit == "gallons":
        if to_unit == "liters":
            return value * 3.78541
        elif to_unit == "milliliters":
            return value * 3785.41
        elif to_unit == "cubic meters":
            return value * 0.00378541
        elif to_unit == "cubic inches":
            return value * 1550.0022
    elif from_unit == "cubic inches":
        if to_unit == "liters":
            return value * 0.0000264172
        elif to_unit == "milliliters":
            return value * 0.0006102374
        elif to_unit == "cubic meters":
            return value * 0.0000000163870673
        elif to_unit == "gallons":
            return value / 1550.0022
    return None
def main():
    sample_value = 10
    from_unit = "liters"
    to_unit = "gallons"
    print(f"Sample Value: {sample_value} {from_unit}")
    converted_value = convert_volume(sample_value, from_unit, to_unit)
    if converted_value is not None:
        print(f"Converted Value: {converted_value:.4f} {to_unit}")
    else:
        print("Invalid conversion requested.")
if __name__ == '__main__':
    main()