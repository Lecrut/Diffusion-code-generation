def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero")
    return kelvin - 273.15

if __name__ == '__main__':
    sample_temperatures = {
        'celsius': 37,
        'fahrenheit': 98.6,
        'kelvin': 310.15
    }
    print(f"{sample_temperatures['celsius']}C is {celsius_to_fahrenheit(sample_temperatures['celsius'])}F")
    print(f"{sample_temperatures['fahrenheit']}F is {fahrenheit_to_celsius(sample_temperatures['fahrenheit'])}C")
    print(f"{sample_temperatures['kelvin']}K is {kelvin_to_celsius(sample_temperatures['kelvin'])}C")