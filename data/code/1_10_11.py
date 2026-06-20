import csv
import io
import tempfile
import os

def parse_numeric_values(text_content):
    parsed_numbers = []
    stream = io.StringIO(text_content)
    reader = csv.reader(stream)
    for row in reader:
        for cell in row:
            trimmed = cell.strip()
            if not trimmed:
                continue
            try:
                number = float(trimmed)
                parsed_numbers.append(number)
            except ValueError:
                continue
    return parsed_numbers

def compute_average(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

def create_sample_csv_file():
    sample_data = """Weight
150.5
160.2
invalid
175.0
abc
180.4
"""
    fd, path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(sample_data)
    return path

class WeightProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_statistics(self):
        values = parse_numeric_values(self._read_file_content())
        average = compute_average(values)
        return {
            "count": len(values),
            "average": average
        }

    def _read_file_content(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

if __name__ == '__main__':
    path = create_sample_csv_file()
    try:
        processor = WeightProcessor(path)
        result = processor.get_statistics()
        print(f"Average weight: {result['average']}")
    finally:
        if os.path.exists(path):
            os.remove(path)