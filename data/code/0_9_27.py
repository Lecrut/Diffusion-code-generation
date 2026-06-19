def convert_lengths(lengths, unit):
    conversion_factors = {
        'kilometers': {'meters': 1000, 'feet': 3280.84},
        'meters': {'meters': 1, 'feet': 3.28084},
        'feet': {'meters': 0.3048, 'feet': 1}
    }
    
    if unit not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    converted_lengths = []
    for length in lengths:
        meters = length * conversion_factors[unit]['meters']
        feet = length * conversion_factors[unit]['feet']
        converted_lengths.append((length, meters, feet))
    
    return converted_lengths

if __name__ == '__main__':
    sample_lengths_km = [1, 2.5, 5]
    unit = 'kilometers'
    conversions = convert_lengths(sample_lengths_km, unit)
    
    for original, meters, feet in conversions:
        print(f"{original} {unit} is equivalent to {meters:.2f} meters and {feet:.2f} feet")