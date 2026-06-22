def validate_temperatures(fahrenheit):
    if not all(isinstance(temp, (int, float)) for temp in fahrenheit):
        raise ValueError("All temperature readings must be numbers.")
    return True

def convert_to_celsius(fahrenheit):
    validate_temperatures(fahrenheit)
    conversion_factor = 5 / 9
    offset = 32
    return tuple(map(lambda f: (f - offset) * conversion_factor, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (45, 86, 130, 220)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)