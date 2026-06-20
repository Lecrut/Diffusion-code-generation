import sys
import io
from pathlib import Path

VOLUME_DATA = """10.5
20.0
bad_value
30.25
-5.0"""

def parse_volume_file(content):
    lines = content.splitlines()
    valid_volumes = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        try:
            value = float(stripped)
            valid_volumes.append(value)
        except ValueError:
            continue
    return valid_volumes

def calculate_total(volumes):
    total = 0.0
    for vol in volumes:
        total += vol
    return total

def process_volume_content(content):
    volumes = parse_volume_file(content)
    total = calculate_total(volumes)
    return total

if __name__ == '__main__':
    content = VOLUME_DATA
    result = process_volume_content(content)
    print(result)