import csv
import io
import tempfile
import os

class WeightAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_and_clean_weights(self):
        weights = []
        with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for cell in row:
                    value = cell.strip()
                    if not value:
                        continue
                    try:
                        num = float(value)
                        weights.append(num)
                    except ValueError:
                        continue
        return weights

    def calculate_average(self):
        clean_weights = self.load_and_clean_weights()
        if not clean_weights:
            return 0.0
        return sum(clean_weights) / len(clean_weights)

def create_sample_csv():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8')
    content = "weight,extra_column\n65.5,active\n70,rest\ninvalid,skip\n82.5,high\n45,low\n\n"
    temp_file.write(content)
    temp_file.close()
    return temp_file.name

if __name__ == '__main__':
    sample_path = create_sample_csv()
    try:
        analyzer = WeightAnalyzer(sample_path)
        result = analyzer.calculate_average()
        print(f"Average weight: {result}")
    finally:
        os.remove(sample_path)