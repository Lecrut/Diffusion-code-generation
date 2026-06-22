def convert_length(lengths, unit):
    meters_per_kilometer = 1000
    feet_per_meter = 3.28084
    
    if unit == 'kilometers':
        conversion_factor_meters = meters_per_kilometer
        conversion_factor_feet = meters_per_kilometer * feet_per_meter
    else:
        raise ValueError("Unsupported unit")
    
    converted_lengths = []
    for length in lengths:
        meters = length * conversion_factor_meters
        feet = length * conversion_factor_feet
        converted_lengths.append((meters, feet))
    
    return converted_lengths

if __name__ == '__main__':
    sample_lengths = [1.0, 2.5, 3.75]
    unit = 'kilometers'
    converted = convert_length(sample_lengths, unit)
    for length in sample_lengths:
        meters, feet = convert_length([length], unit)[0]
        print(f"{length} {unit} is equivalent to {meters:.2f} meters and {feet:.2f} feet")