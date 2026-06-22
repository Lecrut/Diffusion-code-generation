def celsius_to_kelvin(celsius):
    OFFSET = 273.15
    return celsius + OFFSET

if __name__ == '__main__':
    sample_values = {
        'freezing': 0,
        'boiling': 100,
        'absolute_zero': -273.15,
        'human_body': 37
    }
    
    for name, value in sample_values.items():
        print(f"{name}: {value}C is {celsius_to_kelvin(value)}K")