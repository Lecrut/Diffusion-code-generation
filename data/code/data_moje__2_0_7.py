import json
import os

class VolumeCalculator:
    def __init__(self, file_path):
        self.file_path = file_path

    def calculate_total_volume(self):
        if not os.path.exists(self.file_path):
            return 0.0
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            data = json.loads(content)
            if isinstance(data, list):
                total = 0.0
                for item in data:
                    if isinstance(item, dict) and 'volume' in item:
                        value = item['volume']
                        try:
                            total += float(value)
                        except (ValueError, TypeError):
                            continue
                return total
            elif isinstance(data, dict) and 'volumes' in data:
                total = 0.0
                for item in data['volumes']:
                    if isinstance(item, dict) and 'volume' in item:
                        value = item['volume']
                        try:
                            total += float(value)
                        except (ValueError, TypeError):
                            continue
                return total
            elif isinstance(data, dict):
                total = 0.0
                for key, value in data.items():
                    if key.lower().startswith('volume'):
                        try:
                            total += float(value)
                        except (ValueError, TypeError):
                            continue
                return total
            else:
                try:
                    return float(data)
                except (ValueError, TypeError):
                    return 0.0
        except (json.JSONDecodeError, IOError, PermissionError):
            return 0.0

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "volume": 10.5},
        {"id": 2, "volume": 20.3},
        {"id": 3, "volume": 5.2}
    ]
    temp_file = "temp_volumes.json"
    with open(temp_file, 'w') as f:
        json.dump(sample_data, f)
    calculator = VolumeCalculator(temp_file)
    result = calculator.calculate_total_volume()
    print(result)
    os.remove(temp_file)