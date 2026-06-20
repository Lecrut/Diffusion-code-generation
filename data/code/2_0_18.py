import os
import tempfile

DEFAULT_ERROR_RESULT = 0.0

def parse_volume_lines(content):
    lines = content.splitlines()
    volumes = []
    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            val = float(cleaned)
            if val >= 0:
                volumes.append(val)
        except ValueError:
            continue
    return volumes

def calculate_total_volume(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
        parsed = parse_volume_lines(data)
        return sum(parsed)
    except FileNotFoundError:
        return DEFAULT_ERROR_RESULT
    except PermissionError:
        return DEFAULT_ERROR_RESULT
    except IOError:
        return DEFAULT_ERROR_RESULT

class VolumeProcessor:
    def __init__(self, path):
        self.path = path

    def process(self):
        return calculate_total_volume(self.path)

if __name__ == '__main__':
    sample_data = "10.5\n20.0\nabc\n-5.0\n\n30.5"
    fd, temp_path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as tmp:
            tmp.write(sample_data)
        processor = VolumeProcessor(temp_path)
        result = processor.process()
        print(result)
    finally:
        os.unlink(temp_path)