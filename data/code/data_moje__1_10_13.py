import csv
import io

def calculate_average_weight(csv_content):
    total_weight = 0.0
    count = 0
    try:
        reader = csv.reader(io.StringIO(csv_content))
        next(reader, None)
        for row in reader:
            if row:
                try:
                    weight = float(row[0].strip())
                    total_weight += weight
                    count += 1
                except (ValueError, IndexError):
                    continue
    except Exception:
        return 0.0
    if count == 0:
        return 0.0
    return total_weight / count

if __name__ == '__main__':
    sample_csv = "weight\n70.5\n80.2\ninvalid\n65.0\n"
    average = calculate_average_weight(sample_csv)
    print(average)