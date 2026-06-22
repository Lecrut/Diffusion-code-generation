import csv
import io

class DataPipeline:
    def __init__(self, csv_content, factor):
        self.csv_content = csv_content
        self.factor = factor

    def process(self):
        output_buffer = io.StringIO()
        reader = csv.DictReader(io.StringIO(self.csv_content))
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(output_buffer, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            try:
                original_volume = float(row['volume'])
                scaled_volume = original_volume * self.factor
                row['volume'] = scaled_volume
            except (ValueError, KeyError):
                continue
            writer.writerow(row)
        
        return output_buffer.getvalue()

if __name__ == '__main__':
    sample_csv = "name,volume\nApple,10\nBanana,20\nCherry,5"
    scaling_factor = 2.5
    pipeline = DataPipeline(sample_csv, scaling_factor)
    result = pipeline.process()
    print(result)