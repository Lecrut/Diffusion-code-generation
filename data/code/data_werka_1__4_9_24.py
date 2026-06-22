def convert_distance(distance, from_unit, to_unit, conversion_factor):
    if from_unit == 'miles' and to_unit == 'kilometers':
        return distance * conversion_factor
    elif from_unit == 'kilometers' and to_unit == 'miles':
        return distance / conversion_factor
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_distance = 10.0
    from_unit = 'miles'
    to_unit = 'kilometers'
    conversion_factor = 1.60934

    converted_distance = convert_distance(sample_distance, from_unit, to_unit, conversion_factor)
    print(f"{sample_distance} {from_unit} is equal to {converted_distance:.2f} {to_unit}")