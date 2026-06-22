def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero")
    return kelvin - 273.15

if __name__ == '__main__':
    conversion_samples = {
        'celsius': 150,
        'fahrenheit': 68,
        'kelvin': 473.15
    }
    print(f"{conversion_samples['celsius']}C is {celsius_to_fahrenheit(conversion_samples['celsius'])}F")
    print(f"{conversion_samples['fahrenheit']}F is {fahrenheit_to_celsius(conversion_samples['fahrenheit'])}C")
    print(f"{conversion_samples['kelvin']}K is {kelvin_to_celsius(conversion_samples['kelvin'])}C")