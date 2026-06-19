def convert_length(lengths, unit):
    conversion_factors = {
        'kilometers': {'meters': 1000, 'feet': 3280.84},
        'meters': {'meters': 1, 'feet': 3.28084},
        'feet': {'meters': 0.3048, 'feet': 1}
    }
    
    if unit not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    results = []
    for length in lengths:
        meters = length * conversion_factors[unit]['meters']
        feet = length * conversion_factors[unit]['feet']
        results.append((length, meters, feet))
    
    return results

if __name__ == '__main__':
    sample_lengths = [1, 2.5, 10]
    unit = 'kilometers'
    converted_lengths = convert_length(sample_lengths, unit)
    for length, meters, feet in converted_lengths:
        print(f"{length} {unit} is equivalent to {meters:.2f} meters and {feet:.2f} feet")