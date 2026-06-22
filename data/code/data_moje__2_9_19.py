import re

def calculate_total_volume(file_content):
    total_volume = 0.0
    lines = file_content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            value = float(line)
            total_volume += value
        except ValueError:
            match = re.search(r'[-+]?\d*\.?\d+', line)
            if match:
                value = float(match.group())
                total_volume += value
    return total_volume

if __name__ == '__main__':
    sample_data = """10.5
20
3.75
invalid_entry
45.25
error_no_numbers
12.0
"""
    result = calculate_total_volume(sample_data)
    print(result)