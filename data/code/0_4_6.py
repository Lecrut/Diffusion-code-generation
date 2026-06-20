def meters_to_yards(meters):
    return meters * 1.09361

def process_lengths_from_file(filename):
    with open(filename, 'r') as file:
        lengths = [float(line.strip()) for line in file if line.strip()]
    return [meters_to_yards(length) for length in lengths]

if __name__ == '__main__':
    import os
    import tempfile
    sample_data = [1.0, 5.0, 10.5, 25.0]
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        for value in sample_data:
            temp_file.write(str(value) + '\n')
        temp_filename = temp_file.name
    try:
        results = process_lengths_from_file(temp_filename)
        for original, converted in zip(sample_data, results):
            print(f"{original} meters = {converted} yards")
    finally:
        os.remove(temp_filename)