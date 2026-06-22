def liters_to_milliliters(liters):
    return liters * 1000

def liters_to_cubic_meters(liters):
    return liters / 1000

def liters_to_gallons(liters):
    return liters * 0.264172

def liters_to_cubic_inches(liters):
    return liters * 61.0237

def gallons_to_liters(gallons):
    return gallons / 0.264172

def milliliters_to_liters(milliliters):
    return milliliters / 1000

def cubic_meters_to_liters(cubic_meters):
    return cubic_meters * 1000

def cubic_inches_to_liters(cubic_inches):
    return cubic_inches / 61.0237

def convert_volume(value, from_unit, to_unit):
    liters = 0
    if from_unit == "liters":
        liters = value
    elif from_unit == "milliliters":
        liters = milliliters_to_liters(value)
    elif from_unit == "cubic_meters":
        liters = cubic_meters_to_liters(value)
    elif from_unit == "gallons":
        liters = gallons_to_liters(value)
    elif from_unit == "cubic_inches":
        liters = cubic_inches_to_liters(value)
    
    if to_unit == "liters":
        return liters
    elif to_unit == "milliliters":
        return liters_to_milliliters(liters)
    elif to_unit == "cubic_meters":
        return liters_to_cubic_meters(liters)
    elif to_unit == "gallons":
        return liters_to_gallons(liters)
    elif to_unit == "cubic_inches":
        return liters_to_cubic_inches(liters)

if __name__ == '__main__':
    print(convert_volume(1, "liters", "milliliters"))
    print(convert_volume(1, "gallons", "liters"))
    print(convert_volume(1, "cubic_meters", "liters"))
    print(convert_volume(1, "cubic_inches", "liters"))
    print(convert_volume(500, "milliliters", "liters"))