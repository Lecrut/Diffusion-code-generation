def celsius_to_kelvin(celsius):
    KELVIN_OFFSET = 273.15
    return celsius + KELVIN_OFFSET

if __name__ == '__main__':
    sample_values = {
        'freezing_point': 0,
        'boiling_point': 100,
        'absolute_zero': -273.15,
        'average_body_temp': 37
    }
    for description, value in sample_values.items():
        print(f"{description}: {value}C is {celsius_to_kelvin(value)}K")