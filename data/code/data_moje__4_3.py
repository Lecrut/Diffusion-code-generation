def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet * 0.3048

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    sample_meters = 10
    sample_feet = meters_to_feet(sample_meters)
    print(f"{sample_meters} meters is {sample_feet} feet")
    
    converted_back = feet_to_meters(sample_feet)
    print(f"{sample_feet} feet is {converted_back} meters")
    
    sample_kg = 5
    sample_lbs = kilograms_to_pounds(sample_kg)
    print(f"{sample_kg} kilograms is {sample_lbs} pounds")
    
    converted_kg = pounds_to_kilograms(sample_lbs)
    print(f"{sample_lbs} pounds is {converted_kg} kilograms")
    
    sample_celsius = 20
    sample_fahrenheit = celsius_to_fahrenheit(sample_celsius)
    print(f"{sample_celsius} degrees Celsius is {sample_fahrenheit} degrees Fahrenheit")
    
    converted_celsius = fahrenheit_to_celsius(sample_fahrenheit)
    print(f"{sample_fahrenheit} degrees Fahrenheit is {converted_celsius} degrees Celsius")