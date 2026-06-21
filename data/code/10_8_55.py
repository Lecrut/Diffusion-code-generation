TEMPERATURE_PRECISION = 2

def calculate_arithmetic_mean(temperature1, temperature2):
    if not (isinstance(temperature1, (int, float)) and isinstance(temperature2, (int, float))):
        raise ValueError("Both temperatures must be numbers")
    mean_value = (temperature1 + temperature2) / 2
    return round(mean_value, TEMPERATURE_PRECISION)

if __name__ == '__main__':
    sample_temperature1 = 35.7
    sample_temperature2 = 40.2
    try:
        mean_temperature = calculate_arithmetic_mean(sample_temperature1, sample_temperature2)
        print(mean_temperature)
    except ValueError as e:
        print(e)