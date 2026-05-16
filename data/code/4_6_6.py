import math
def convert_distance(distance, from_unit, to_unit):
    if from_unit == to_unit:
        return distance
    conversion_factors = {
        ('m', 'km'): 1000,
        ('km', 'm'): 1/1000,
        ('cm', 'm'): 0.01,
        ('m', 'cm'): 100,
        ('m', 'km'): 1/1000,
        ('km', 'm'): 1000
    }
    if (from_unit, to_unit) in conversion_factors:
        return distance * conversion_factors[(from_unit, to_unit)]
    if from_unit == 'm' and to_unit == 'm':
        return distance
    if from_unit == 'km' and to_unit == 'km':
        return distance
    if from_unit == 'cm' and to_unit == 'cm':
        return distance
    raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    sample_distance = 5000
    sample_from_unit = 'm'
    sample_to_unit = 'km'
    try:
        result = convert_distance(sample_distance, sample_from_unit, sample_to_unit)
        print(f"Input Distance: {sample_distance} {sample_from_unit}")
        print(f"Target Unit: {sample_to_unit}")
        print(f"Converted Result: {result:.3f} {sample_to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_2 = 150
    sample_from_unit_2 = 'cm'
    sample_to_unit_2 = 'm'
    try:
        result_2 = convert_distance(sample_distance_2, sample_from_unit_2, sample_to_unit_2)
        print(f"\nInput Distance: {sample_distance_2} {sample_from_unit_2}")
        print(f"Target Unit: {sample_to_unit_2}")
        print(f"Converted Result: {result_2:.3f} {sample_to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_3 = 10
    sample_from_unit_3 = 'm'
    sample_to_unit_3 = 'm'
    try:
        result_3 = convert_distance(sample_distance_3, sample_from_unit_3, sample_to_unit_3)
        print(f"\nInput Distance: {sample_distance_3} {sample_from_unit_3}")
        print(f"Target Unit: {sample_to_unit_3}")
        print(f"Converted Result: {result_3:.3f} {sample_to_unit_3}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_4 = 100
    sample_from_unit_4 = 'km'
    sample_to_unit_4 = 'm'
    try:
        result_4 = convert_distance(sample_distance_4, sample_from_unit_4, sample_to_unit_4)
        print(f"\nInput Distance: {sample_distance_4} {sample_from_unit_4}")
        print(f"Target Unit: {sample_to_unit_4}")
        print(f"Converted Result: {result_4:.3f} {sample_to_unit_4}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")