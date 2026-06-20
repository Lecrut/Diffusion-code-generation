import os
import tempfile

class VolumeCalculator:
    def __init__(self):
        self.volumes = []

    def read_volumes(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.volumes = []
                for line in lines:
                    line = line.strip()
                    if line:
                        try:
                            value = float(line)
                            self.volumes.append(value)
                        except ValueError:
                            continue
                return self.volumes
        except FileNotFoundError:
            return []
        except IOError:
            return []
        except Exception:
            return []

    def calculate_total(self):
        if not self.volumes:
            return 0.0
        total = 0.0
        for volume in self.volumes:
            total += volume
        return total

def create_sample_file(content):
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt')
    temp_file.write(content)
    temp_file.close()
    return temp_file.name

if __name__ == '__main__':
    sample_data = "10.5\n20.3\n15.0\ninvalid\n30.2"
    file_path = create_sample_file(sample_data)
    try:
        calculator = VolumeCalculator()
        calculator.read_volumes(file_path)
        total_volume = calculator.calculate_total()
        print(total_volume)
    finally:
        os.unlink(file_path)