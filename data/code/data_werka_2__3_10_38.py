def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = {
        'freezing': 32,
        'boiling': 212,
        'absolute_zero': -40,
        'room_temp': 72
    }
    
    for description, value in sample_values.items():
        kelvin_value = fahrenheit_to_kelvin(value)
        print(f"{description.capitalize()}: {value}°F is {kelvin_value:.2f}K")