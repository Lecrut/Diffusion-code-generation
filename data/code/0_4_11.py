def convert_meters_to_yards(lengths_meters):
    conversion_factor = 1.09361
    return [length * conversion_factor for length in lengths_meters]

if __name__ == '__main__':
    sample_lengths = [1.0, 2.5, 10.0, 100.0]
    sample_lines = "\n".join(map(str, sample_lengths))
    with open('input_lengths.txt', 'w') as f:
        f.write(sample_lines)
    
    with open('input_lengths.txt', 'r') as f:
        file_content = f.read()
    
    parsed_lengths = [float(line.strip()) for line in file_content.splitlines() if line.strip()]
    yard_lengths = convert_meters_to_yards(parsed_lengths)
    print(yard_lengths)