import csv
import io
from statistics import mean

class WeightProcessor:
    def __init__(self):
        self.weights = []

    def parse_csv_content(self, csv_data):
        reader = csv.reader(io.StringIO(csv_data))
        for row in reader:
            for cell in row:
                cleaned = cell.strip()
                if not cleaned:
                    continue
                try:
                    value = float(cleaned)
                    self.weights.append(value)
                except ValueError:
                    continue

    def get_average(self):
        if not self.weights:
            return 0.0
        return mean(self.weights)

SAMPLE_CSV_DATA = """id,weight,notes
1,65.5,healthy
2,invalid,skip
3,70.0,good
4,68.5,ok
5,not_a_number,error
6,72.0,high"""

if __name__ == '__main__':
    processor = WeightProcessor()
    processor.parse_csv_content(SAMPLE_CSV_DATA)
    result = processor.get_average()
    print(result)