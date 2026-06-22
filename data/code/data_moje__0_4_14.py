def convert_meters_to_yards(meters):
    return meters * 1.09361

def process_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    results = []
    for line in lines:
        try:
            value = float(line.strip())
            converted = convert_meters_to_yards(value)
            results.append(converted)
        except ValueError:
            continue
    return results

if __name__ == '__main__':
    import os
    import tempfile
    sample_values = [1.0, 10.0, 100.0]
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        for val in sample_values:
            tmp.write(f"{val}\n")
        temp_path = tmp.name
    try:
        converted_values = process_file(temp_path)
        for val in converted_values:
            print(val)
    finally:
        os.remove(temp_path)