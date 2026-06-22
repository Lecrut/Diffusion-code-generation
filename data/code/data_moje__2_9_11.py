import tempfile
import os

def parse_volumes_from_content(content):
    valid_values = []
    lines = content.split('\n')
    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            value = float(cleaned)
            valid_values.append(value)
        except ValueError:
            continue
    return valid_values

def compute_total_volume(values):
    if not values:
        return 0.0
    return sum(values)

class VolumeAnalyzer:
    def __init__(self, raw_content):
        self.raw_content = raw_content
        self.parsed_data = parse_volumes_from_content(raw_content)

    def get_valid_entries(self):
        return self.parsed_data

    def calculate_sum(self):
        return compute_total_volume(self.parsed_data)

if __name__ == '__main__':
    sample_data = """10.5
20.0
invalid_input
30.25
-5.0
empty_line_here

15.5"""
    analyzer = VolumeAnalyzer(sample_data)
    entries = analyzer.get_valid_entries()
    total = analyzer.calculate_sum()
    print(entries)
    print(total)