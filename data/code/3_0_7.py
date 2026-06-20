import csv
import tempfile
import os

class TemperatureAnalyzer:
    def __init__(self):
        self.readings = []

    def load_from_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        self.readings = []
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                if 'temperature' not in reader.fieldnames:
                    raise ValueError("CSV must contain 'temperature' column")
                for row in reader:
                    try:
                        val = float(row['temperature'])
                        self.readings.append(val)
                    except ValueError:
                        continue
        except IOError as e:
            raise IOError(f"Error reading file: {e}")
        
        if not self.readings:
            raise ValueError("No valid temperature readings could be parsed from the file.")

    def calculate_average(self):
        if not self.readings:
            return 0.0
        return sum(self.readings) / len(self.readings)

    def get_reading_count(self):
        return len(self.readings)

def create_sample_data():
    fd, path = tempfile.mkstemp(suffix='.csv')
    try:
        with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'temperature', 'location'])
            writer.writerow(['2023-10-01', '20.5', 'A'])
            writer.writerow(['2023-10-02', '22.0', 'B'])
            writer.writerow(['2023-10-03', '19.5', 'C'])
            writer.writerow(['2023-10-04', 'invalid', 'D'])
            writer.writerow(['2023-10-05', '21.0', 'E'])
        return path
    except Exception:
        os.close(fd)
        raise

if __name__ == '__main__':
    temp_file_path = create_sample_data()
    analyzer = TemperatureAnalyzer()
    try:
        analyzer.load_from_file(temp_file_path)
        count = analyzer.get_reading_count()
        average = analyzer.calculate_average()
        print(f"Count: {count}")
        print(f"Average: {average}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)