import tempfile
import os

class LengthConverter:
    METERS_TO_YARDS_FACTOR = 1.09361

    def __init__(self, source_path):
        self.source_path = source_path

    def read_lengths(self):
        with open(self.source_path, 'r') as f:
            raw_lines = f.readlines()
        lengths = []
        for line in raw_lines:
            cleaned = line.strip()
            if cleaned:
                try:
                    val = float(cleaned)
                    lengths.append(val)
                except ValueError:
                    continue
        return lengths

    def convert_all(self, lengths):
        results = []
        for length in lengths:
            yards = length * self.METERS_TO_YARDS_FACTOR
            results.append(yards)
        return results

    def process(self):
        meters = self.read_lengths()
        return self.convert_all(meters)

if __name__ == '__main__':
    sample_values = [1.0, 5.5, 100.25, 0.0]
    fd, temp_path = tempfile.mkstemp(suffix='.txt')
    try:
        with os.fdopen(fd, 'w') as f:
            for val in sample_values:
                f.write(str(val) + '\n')
        converter = LengthConverter(temp_path)
        output_yards = converter.process()
        for y in output_yards:
            print(y)
    finally:
        os.unlink(temp_path)