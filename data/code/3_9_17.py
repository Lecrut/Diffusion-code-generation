def convert_temp(celsius_readings):
    conversion_factors = {
        'scale_multiplier': 9.0 / 5.0,
        'offset': 32.0
    }
    return [c * conversion_factors['scale_multiplier'] + conversion_factors['offset'] for c in celsius_readings]

if __name__ == '__main__':
    sample_data = [-40.0, 0.0, 10.0, 25.0, 37.0, 100.0]
    computed_fahrenheit = convert_temp(sample_data)
    print(computed_fahrenheit)