def convert_meters_to_yards(meters):
    return meters * 1.09361

def read_lengths_from_content(content):
    results = []
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        try:
            value = float(stripped)
            converted = convert_meters_to_yards(value)
            results.append(converted)
        except ValueError:
            continue
    return results

if __name__ == '__main__':
    sample_data = """1.0
10.5
0.5
20
invalid"""
    output_values = read_lengths_from_content(sample_data)
    for val in output_values:
        print(val)