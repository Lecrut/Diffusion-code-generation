import csv
import tempfile
import os

class VolumeScaler:
    def __init__(self, input_file, output_file, scale_factor):
        self.input_file = input_file
        self.output_file = output_file
        self.scale_factor = scale_factor

    def process(self):
        rows = []
        with open(self.input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                try:
                    volume = float(row['volume'])
                except (ValueError, KeyError):
                    continue
                scaled_volume = volume * self.scale_factor
                rows.append({'name': row['name'], 'volume': scaled_volume})
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['name', 'volume'])
            writer.writeheader()
            writer.writerows(rows)
        return len(rows)

if __name__ == '__main__':
    sample_csv_content = "name,volume\nApple,10.5\nBanana,20.0\nCherry,5.5\n"
    csv_filename = 'sample_data.csv'
    with open(csv_filename, 'w', encoding='utf-8') as f:
        f.write(sample_csv_content)
    
    scaler = VolumeScaler(csv_filename, 'scaled_data.csv', 2.5)
    processed_count = scaler.process()
    
    results = []
    with open('scaled_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(f"{row['name']}: {row['volume']}")
    
    print(f"Processed {processed_count} items")
    for r in results:
        print(r)
    
    os.remove(csv_filename)
    os.remove('scaled_data.csv')