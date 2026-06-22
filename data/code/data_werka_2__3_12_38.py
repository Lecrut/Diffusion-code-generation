def celsius_to_kelvin(celsius):
    return celsius + 273.15

if __name__ == '__main__':
    temperature_samples = {
        'freezing_point': 0,
        'boiling_point': 100,
        'absolute_zero': -273.15,
        'average_human_body_temp': 37
    }
    
    for description, celsius_value in temperature_samples.items():
        kelvin_value = celsius_to_kelvin(celsius_value)
        print(f"{description}: {celsius_value}°C is {kelvin_value}K")