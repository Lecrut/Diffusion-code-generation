KELVIN_OFFSET = 273.15
FAHRENHEIT_MULTIPLIER = 1.8
FAHRENHEIT_OFFSET = 32.0

def _validate_temp(value, name, min_val):
    if value < min_val:
        raise ValueError(f"{name} {value} is below absolute zero.")
    return value

def celsius_to_fahrenheit(celsius):
    _validate_temp(celsius, "Celsius", -273.15)
    return celsius * FAHRENHEIT_MULTIPLIER + FAHRENHEIT_OFFSET

def fahrenheit_to_celsius(fahrenheit):
    _validate_temp(fahrenheit, "Fahrenheit", -459.67)
    return (fahrenheit - FAHRENHEIT_OFFSET) / FAHRENHEIT_MULTIPLIER

def kelvin_to_celsius(kelvin):
    _validate_temp(kelvin, "Kelvin", 0)
    return kelvin - KELVIN_OFFSET

if __name__ == '__main__':
    val_c = 25.0
    val_f = -40.0
    val_k = 0.0
    
    res_f = celsius_to_fahrenheit(val_c)
    res_c = fahrenheit_to_celsius(val_f)
    res_k = kelvin_to_celsius(val_k)
    
    print(res_f)
    print(res_c)
    print(res_k)