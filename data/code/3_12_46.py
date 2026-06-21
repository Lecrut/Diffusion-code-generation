def celsius_to_kelvin(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not possible")
    kelvin = celsius + 273.15
    return kelvin

if __name__ == '__main__':
    sample_temperatures = {
        'freezing_point': 0,
        'boiling_point': 100,
        'human_body_temperature': 37,
        'subzero_example': -10
    }
    for description, celsius in sample_temperatures.items():
        kelvin = celsius_to_kelvin(celsius)
        print(f"{description}: {celsius}C is {kelvin}K")