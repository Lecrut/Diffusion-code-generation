def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero")
    return kelvin - 273.15

if __name__ == '__main__':
    sample_values = {
        'celsius': 45,
        'fahrenheit': 113,
        'kelvin': 318.15
    }
    
    print(f"{sample_values['celsius']}C is {celsius_to_fahrenheit(sample_values['celsius'])}F")
    print(f"{sample_values['fahrenheit']}F is {fahrenheit_to_celsius(sample_values['fahrenheit'])}C")
    print(f"{sample_values['kelvin']}K is {kelvin_to_celsius(sample_values['kelvin'])}C")