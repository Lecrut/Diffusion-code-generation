def validate_temperatures(fahrenheit):
    if not isinstance(fahrenheit, tuple):
        raise ValueError("Input must be a tuple.")
    for temp in fahrenheit:
        if not isinstance(temp, (int, float)):
            raise ValueError("All elements in the tuple must be numbers.")

def convert_to_celsius(fahrenheit):
    validate_temperatures(fahrenheit)
    conversion_factor = 5 / 9
    offset = 32
    return tuple(map(lambda f: (f - offset) * conversion_factor, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (45, 86, 130, 374)
    try:
        celsius_temperatures = convert_to_celsius(sample_temperatures)
        print(celsius_temperatures)
    except ValueError as e:
        print(e)