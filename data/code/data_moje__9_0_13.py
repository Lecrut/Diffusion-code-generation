def convert_liters_to_liters(value):
    return value

def convert_liters_to_milliliters(value):
    return value * 1000

def convert_liters_to_cubic_meters(value):
    return value / 1000

def convert_liters_to_gallons(value):
    return value * 0.264172

def convert_liters_to_cubic_inches(value):
    return value * 61.0237

def convert_milliliters_to_liters(value):
    return value / 1000

def convert_milliliters_to_milliliters(value):
    return value

def convert_milliliters_to_cubic_meters(value):
    return value / 1000000

def convert_milliliters_to_gallons(value):
    return value * 0.000264172

def convert_milliliters_to_cubic_inches(value):
    return value * 0.0610237

def convert_cubic_meters_to_liters(value):
    return value * 1000

def convert_cubic_meters_to_milliliters(value):
    return value * 1000000

def convert_cubic_meters_to_cubic_meters(value):
    return value

def convert_cubic_meters_to_gallons(value):
    return value * 264.172

def convert_cubic_meters_to_cubic_inches(value):
    return value * 61023.7

def convert_gallons_to_liters(value):
    return value / 0.264172

def convert_gallons_to_milliliters(value):
    return value / 0.264172 * 1000

def convert_gallons_to_cubic_meters(value):
    return value / 264.172

def convert_gallons_to_gallons(value):
    return value

def convert_gallons_to_cubic_inches(value):
    return value * 231

def convert_cubic_inches_to_liters(value):
    return value / 61.0237

def convert_cubic_inches_to_milliliters(value):
    return value / 61.0237 * 1000

def convert_cubic_inches_to_cubic_meters(value):
    return value / 61023.7

def convert_cubic_inches_to_gallons(value):
    return value / 231

def convert_cubic_inches_to_cubic_inches(value):
    return value

def convert_volume_from_liters(source, target, value):
    if source == "liters":
        if target == "liters":
            return convert_liters_to_liters(value)
        elif target == "milliliters":
            return convert_liters_to_milliliters(value)
        elif target == "cubic_meters":
            return convert_liters_to_cubic_meters(value)
        elif target == "gallons":
            return convert_liters_to_gallons(value)
        elif target == "cubic_inches":
            return convert_liters_to_cubic_inches(value)
    elif source == "milliliters":
        if target == "liters":
            return convert_milliliters_to_liters(value)
        elif target == "milliliters":
            return convert_milliliters_to_milliliters(value)
        elif target == "cubic_meters":
            return convert_milliliters_to_cubic_meters(value)
        elif target == "gallons":
            return convert_milliliters_to_gallons(value)
        elif target == "cubic_inches":
            return convert_milliliters_to_cubic_inches(value)
    elif source == "cubic_meters":
        if target == "liters":
            return convert_cubic_meters_to_liters(value)
        elif target == "milliliters":
            return convert_cubic_meters_to_milliliters(value)
        elif target == "cubic_meters":
            return convert_cubic_meters_to_cubic_meters(value)
        elif target == "gallons":
            return convert_cubic_meters_to_gallons(value)
        elif target == "cubic_inches":
            return convert_cubic_meters_to_cubic_inches(value)
    elif source == "gallons":
        if target == "liters":
            return convert_gallons_to_liters(value)
        elif target == "milliliters":
            return convert_gallons_to_milliliters(value)
        elif target == "cubic_meters":
            return convert_gallons_to_cubic_meters(value)
        elif target == "gallons":
            return convert_gallons_to_gallons(value)
        elif target == "cubic_inches":
            return convert_gallons_to_cubic_inches(value)
    elif source == "cubic_inches":
        if target == "liters":
            return convert_cubic_inches_to_liters(value)
        elif target == "milliliters":
            return convert_cubic_inches_to_milliliters(value)
        elif target == "cubic_meters":
            return convert_cubic_inches_to_cubic_meters(value)
        elif target == "gallons":
            return convert_cubic_inches_to_gallons(value)
        elif target == "cubic_inches":
            return convert_cubic_inches_to_cubic_inches(value)
    return value

if __name__ == '__main__':
    print(convert_volume_from_liters("liters", "milliliters", 5))
    print(convert_volume_from_liters("gallons", "liters", 10))
    print(convert_volume_from_liters("cubic_meters", "gallons", 2))
    print(convert_volume_from_liters("cubic_inches", "liters", 500))
    print(convert_volume_from_liters("milliliters", "cubic_meters", 50000))