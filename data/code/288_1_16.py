CONVERSIONS = {'Celsius': {'Fahrenheit': lambda t: t * 9 / 5 + 32, 'Kelvin': lambda t: t + 273.15}, 'Fahrenheit': {'Celsius': lambda t: (t - 32) * 5 / 9, 'Kelvin': lambda t: (t - 32) * 5 / 9 + 273.15}, 'Kelvin': {'Celsius': lambda t: t - 273.15, 'Fahrenheit': lambda t: (t - 273.15) * 9 / 5 + 32}}

def convert_temp(temp, source_scale):
    if source_scale not in CONVERSIONS:
        raise ValueError('Unsupported source scale')
    return {target_scale: converter(temp) for target_scale, converter in CONVERSIONS[source_scale].items()}
if __name__ == '__main__':
    sample_temp = 20
    sample_scale = 'Celsius'
    converted_values = convert_temp(sample_temp, sample_scale)
    print(converted_values)