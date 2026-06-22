import argparse

def convert_volume(input_volume, input_unit, output_unit):
    conversion_factors = {'m3': {'m3': 1, 'liters': 1000}, 'liters': {'m3': 0.001, 'liters': 1}}
    if input_unit not in conversion_factors or output_unit not in conversion_factors[input_unit]:
        raise ValueError('Invalid unit specified')
    return input_volume * conversion_factors[input_unit][output_unit]

def main():
    sample_input_volume = 2.5
    sample_input_unit = 'm3'
    sample_output_unit = 'liters'
    try:
        result = convert_volume(sample_input_volume, sample_input_unit, sample_output_unit)
        print(result)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    main()