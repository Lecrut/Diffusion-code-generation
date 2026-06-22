def celsius_to_kelvin(celsius):
    conversion_table = {
        'celsius_offset': 273.15
    }
    return celsius + conversion_table['celsius_offset']

if __name__ == '__main__':
    sample_values = {
        'freezing_point_water': 0,
        'boiling_point_water': 100,
        'absolute_zero': -273.15,
        'average_body_temperature': 37
    }
    for description, value in sample_values.items():
        print(f"{description}: {value}C is {celsius_to_kelvin(value)}K")