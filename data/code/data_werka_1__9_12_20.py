import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {'m3': {'m3': 1, 'cm3': 1000000.0, 'L': 1000}, 'cm3': {'m3': 1e-06, 'cm3': 1, 'L': 1}, 'L': {'m3': 0.001, 'cm3': 1, 'L': 1}}
    if input_unit not in conversion_factors or output_unit not in conversion_factors[input_unit]:
        raise ValueError('Invalid unit specified')
    return volume * conversion_factors[input_unit][output_unit]

def main():
    sample_volume = 5.0
    sample_input_unit = 'm3'
    sample_output_unit = 'L'
    try:
        converted_volume = convert_volume(sample_volume, sample_input_unit, sample_output_unit)
        print(converted_volume)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    main()