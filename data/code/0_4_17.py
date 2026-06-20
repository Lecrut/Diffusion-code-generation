import tempfile
import os

METERS_PER_YARD = 0.9144

class LengthConverter:
    def __init__(self):
        self.history = []

    def convert_meters_to_yards(self, meters):
        return meters / METERS_PER_YARD

    def process_list(self, meter_values):
        results = []
        for value in meter_values:
            yards = self.convert_meters_to_yards(value)
            results.append(yards)
            self.history.append((value, yards))
        return results

    def get_history(self):
        return self.history

def create_temp_file(values):
    fd, path = tempfile.mkstemp(suffix='.txt')
    try:
        with os.fdopen(fd, 'w') as f:
            for v in values:
                f.write(str(v) + '\n')
        return path
    except Exception:
        os.close(fd)
        raise

def read_and_convert(filepath, converter):
    with open(filepath, 'r') as f:
        raw_lines = f.readlines()
    
    parsed_lengths = []
    for line in raw_lines:
        clean_line = line.strip()
        if clean_line:
            try:
                num = float(clean_line)
                parsed_lengths.append(num)
            except ValueError:
                continue
    
    return converter.process_list(parsed_lengths)

if __name__ == '__main__':
    sample_data = [1.0, 10.0, 5.5, 100.0, 0.25]
    temp_path = create_temp_file(sample_data)
    
    converter = LengthConverter()
    yard_values = read_and_convert(temp_path, converter)
    
    for y in yard_values:
        print(y)
    
    os.remove(temp_path)