def liters_to_milliliters(liters):
    return liters * 1000

def liters_to_cubic_meters(liters):
    return liters / 1000

def liters_to_gallons(liters):
    return liters * 0.264172

def liters_to_cubic_inches(liters):
    return liters * 61.0237

def milliliters_to_liters(milliliters):
    return milliliters / 1000

def cubic_meters_to_liters(cubic_meters):
    return cubic_meters * 1000

def gallons_to_liters(gallons):
    return gallons / 0.264172

def cubic_inches_to_liters(cubic_inches):
    return cubic_inches / 61.0237

def convert_volume(value, from_unit, to_unit):
    liters = 0.0
    if from_unit == "ml":
        liters = milliliters_to_liters(value)
    elif from_unit == "m3":
        liters = cubic_meters_to_liters(value)
    elif from_unit == "gal":
        liters = gallons_to_liters(value)
    elif from_unit == "in3":
        liters = cubic_inches_to_liters(value)
    elif from_unit == "l":
        liters = value
    else:
        raise ValueError("Unsupported source unit")

    if to_unit == "ml":
        return liters_to_milliliters(liters)
    elif to_unit == "m3":
        return liters_to_cubic_meters(liters)
    elif to_unit == "gal":
        return liters_to_gallons(liters)
    elif to_unit == "in3":
        return liters_to_cubic_inches(liters)
    elif to_unit == "l":
        return liters
    else:
        raise ValueError("Unsupported target unit")

if __name__ == '__main__':
    sample_value = 5.0
    sample_from = "l"
    sample_to = "gal"
    result = convert_volume(sample_value, sample_from, sample_to)
    print(result)
    sample_value_two = 1000
    sample_from_two = "ml"
    sample_to_two = "l"
    result_two = convert_volume(sample_value_two, sample_from_two, sample_to_two)
    print(result_two)
    sample_value_three = 1
    sample_from_three = "m3"
    sample_to_three = "in3"
    result_three = convert_volume(sample_value_three, sample_from_three, sample_to_three)
    print(result_three)