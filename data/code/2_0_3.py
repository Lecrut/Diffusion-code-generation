import os
import tempfile

class VolumeCalculator:
    def __init__(self, file_path):
        self.file_path = file_path

    def calculate_total_volume(self):
        total_volume = 0.0
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        volume_value = float(line)
                        total_volume += volume_value
                    except ValueError:
                        continue
            return total_volume
        except FileNotFoundError:
            return 0.0
        except PermissionError:
            return 0.0
        except Exception:
            return 0.0

if __name__ == '__main__':
    temp_dir = tempfile.mkdtemp()
    sample_file_path = os.path.join(temp_dir, "volumes.txt")
    with open(sample_file_path, 'w') as f:
        f.write("10.5\n")
        f.write("20.0\n")
        f.write("5.5\n")
        f.write("invalid_line\n")
        f.write("30.0\n")
    
    calculator = VolumeCalculator(sample_file_path)
    result = calculator.calculate_total_volume()
    print(result)
    
    os.remove(sample_file_path)
    os.rmdir(temp_dir)