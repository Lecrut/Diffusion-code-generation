def _validate_positive(value):
    if value <= 0:
        raise ValueError("Value must be positive")
    return value

def convert_meters_to_feet(meters):
    validated = _validate_positive(meters)
    return validated * 3.28084

def convert_feet_to_meters(feet):
    validated = _validate_positive(feet)
    return validated / 3.28084

def convert_kilometers_to_miles(kilometers):
    validated = _validate_positive(kilometers)
    return validated * 0.621371

def convert_miles_to_kilometers(miles):
    validated = _validate_positive(miles)
    return validated / 0.621371

def convert_kilograms_to_pounds(kilograms):
    validated = _validate_positive(kilograms)
    return validated * 2.20462

def convert_pounds_to_kilograms(pounds):
    validated = _validate_positive(pounds)
    return validated / 2.20462

def convert_liters_to_gallons(liters):
    validated = _validate_positive(liters)
    return validated * 0.264172

def convert_gallons_to_liters(gallons):
    validated = _validate_positive(gallons)
    return validated / 0.264172

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    print(convert_meters_to_feet(10))
    print(convert_feet_to_meters(32.8084))
    print(convert_kilometers_to_miles(5))
    print(convert_miles_to_kilometers(3.10686))
    print(convert_kilograms_to_pounds(1))
    print(convert_pounds_to_kilograms(2.20462))
    print(convert_liters_to_gallons(1))
    print(convert_gallons_to_liters(0.264172))
    print(convert_celsius_to_fahrenheit(0))
    print(convert_fahrenheit_to_celsius(32))