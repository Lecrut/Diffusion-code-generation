import csv
from typing import List, Tuple
def process_csv(input_file: str) -> List[Tuple[int, float]]:
    results = []
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                original_volume = int(row['volume'])
                converted_liters = float(original_volume / 100.0)
                results.append((original_volume, converted_liters))
            except ValueError as e:
                print(f"Error processing row {row}: {e}")
    return results
def main():
    input_data = [
        "volume,country",
        "50,Brazil",
        "120,Mexico",
        "8,Colombia",
        "45,Venezuela"
    ]
    output_file = 'converted_output.csv'
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['original_volume_liters'])
        for original_vol in input_data[1:]:
            liters = float(original_vol.split(',')[0]) / 100.0
            writer.writerow([liters])
if __name__ == '__main__':
    main()