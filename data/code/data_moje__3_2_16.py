def celsius_to_fahrenheit_dict(temps):
    return {k: v * 9 / 5 + 32 for k, v in temps.items()}

if __name__ == '__main__':
    sample_temps = {"New York": 20, "London": 15, "Tokyo": 25}
    result = celsius_to_fahrenheit_dict(sample_temps)
    print(result)