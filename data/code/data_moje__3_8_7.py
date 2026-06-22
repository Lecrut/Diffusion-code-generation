import csv
import tempfile

def celsius_to_fahrenheit(value):
    return value * 9 / 5 + 32

def read_temperature_csv(filepath):
    with open(filepath, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        if 'temperature_celsius' not in fieldnames:
            raise ValueError("Missing 'temperature_celsius' column")
        rows = []
        for row in reader:
            try:
                c_val = float(row['temperature_celsius'])
                f_val = celsius_to_fahrenheit(c_val)
                new_row = dict(row)
                new_row['temperature_celsius'] = c_val
                new_row['temperature_fahrenheit'] = f_val
                rows.append(new_row)
            except (ValueError, KeyError):
                continue
        return fieldnames, rows

def write_temperature_csv(filepath, fieldnames, rows):
    out_fields = fieldnames + ['temperature_fahrenheit']
    with open(filepath, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=out_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def process_temperatures(input_path, output_path):
    fieldnames, rows = read_temperature_csv(input_path)
    write_temperature_csv(output_path, fieldnames, rows)
    return rows

if __name__ == '__main__':
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as tmp:
        writer = csv.writer(tmp)
        writer.writerow(['temperature_celsius'])
        writer.writerow([0])
        writer.writerow([100])
        tmp.flush()
        temp_path = tmp.name
    results = process_temperatures(temp_path, 'output_temps.csv')
    for r in results:
        print(f"{r['temperature_celsius']} C = {r['temperature_fahrenheit']} F")
    print(len(results))