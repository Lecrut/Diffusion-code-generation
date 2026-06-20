import io

class VolumeCalculator:
    def __init__(self, file_path):
        self.file_path = file_path
        self._content = ""
    
    def _read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                self._content = file.read()
            return True
        except FileNotFoundError:
            self._content = ""
            return False
        except IOError:
            self._content = ""
            return False
    
    def calculate_total(self):
        if not self._read_file():
            return 0.0
        total_volume = 0.0
        lines = self._content.splitlines()
        for line in lines:
            clean_line = line.strip()
            if not clean_line:
                continue
            try:
                value = float(clean_line)
                total_volume += value
            except ValueError:
                continue
        return total_volume

def generate_test_file():
    test_content = "10.5\n20.0\ninvalid\n30.5\n\n45.0\n"
    with open("measurements.txt", "w") as f:
        f.write(test_content)
    return "measurements.txt"

if __name__ == '__main__':
    file_path = generate_test_file()
    calculator = VolumeCalculator(file_path)
    result = calculator.calculate_total()
    print(result)