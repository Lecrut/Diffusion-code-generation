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
    sample_lengths = [1.0, 2.5, 3.7]
    unit = 'kilometers'
    results = convert_length(sample_lengths, unit)
    for length, meters, feet in results:
        print(f"{length} {unit} is equivalent to {meters} meters and {feet} feet")