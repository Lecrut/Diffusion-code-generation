import csv
import io

def scale_volumes(csv_content, scale_factor):
    reader = csv.reader(io.StringIO(csv_content))
    header = next(reader)
    volume_index = header.index('volume')
    rows = []
    for row in reader:
        volume_value = float(row[volume_index])
        scaled_volume = volume_value * scale_factor
        new_row = row[:]
        new_row[volume_index] = str(scaled_volume)
        rows.append(new_row)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(header)
    writer.writerows(rows)
    return output.getvalue()

if __name__ == '__main__':
    sample_csv = "name,volume\nitem1,10.0\nitem2,20.0\nitem3,30.0"
    factor = 2.5
    result = scale_volumes(sample_csv, factor)
    print(result)