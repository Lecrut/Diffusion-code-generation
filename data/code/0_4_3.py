def convert_meters_to_yards(lengths):
    conversion_factor = 1.09361
    results = []
    for length in lengths:
        results.append(length * conversion_factor)
    return results

if __name__ == '__main__':
    sample_lengths = [1.0, 5.0, 10.0, 25.5]
    converted_lengths = convert_meters_to_yards(sample_lengths)
    for original, converted in zip(sample_lengths, converted_lengths):
        print(f"{original} meters is {converted} yards")