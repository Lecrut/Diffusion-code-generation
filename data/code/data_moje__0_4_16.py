import tempfile
import os

YARDS_PER_METER = 1.09361

class LengthConverter:
    def __init__(self, factor=YARDS_PER_METER):
        self.factor = factor

    def convert(self, meters):
        return meters * self.factor

    def convert_batch(self, meters_list):
        return [self.convert(m) for m in meters_list]

def create_temp_file(values):
    fd, path = tempfile.mkstemp(suffix='.txt')
    try:
        with os.fdopen(fd, 'w') as f:
            for val in values:
                f.write(f"{val}\n")
        return path
    except Exception:
        os.close(fd)
        raise

def read_and_convert(filepath, converter):
    results = []
    with open(filepath, 'r') as f:
        for line in f:
            cleaned = line.strip()
            if not cleaned:
                continue
            try:
                val = float(cleaned)
                results.append(converter.convert(val))
            except ValueError:
                continue
    return results

if __name__ == '__main__':
    sample_meters = [10, 25.5, 100, 0.5, 75]
    file_path = create_temp_file(sample_meters)
    try:
        converter = LengthConverter(YARDS_PER_METER)
        output_values = read_and_convert(file_path, converter)
        for orig, conv in zip(sample_meters, output_values):
            print(f"{orig} meters equals {conv} yards")
    finally:
        os.remove(file_path)