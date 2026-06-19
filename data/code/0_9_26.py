def convert_length(lengths, unit):
    if unit == 'kilometers':
        conversion_factors = {'meters': 1000, 'feet': 3280.84}
    else:
        raise ValueError("Unsupported unit")

    converted_lengths = []
    for length in lengths:
        meters = length * conversion_factors['meters']
        feet = length * conversion_factors['feet']
        converted_lengths.append((length, meters, feet))
    
    return converted_lengths

if __name__ == '__main__':
    sample_lengths_km = [1.0, 2.5, 3.75]
    unit = 'kilometers'
    results = convert_length(sample_lengths_km, unit)
    for length_km, length_m, length_ft in results:
        print(f"{length_km} {unit} is equivalent to {length_m} meters and {length_ft} feet")