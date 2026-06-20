import csv
import io

def scale_volumes(csv_content, scale_factor):
    input_stream = io.StringIO(csv_content)
    reader = csv.reader(input_stream)
    header = next(reader)
    output_rows = [header]
    for row in reader:
        if len(row) >= 2:
            try:
                item_name = row[0]
                original_volume = float(row[1])
                scaled_volume = original_volume * scale_factor
                output_rows.append([item_name, scaled_volume])
            except (ValueError, IndexError):
                output_rows.append(row)
    output_stream = io.StringIO()
    writer = csv.writer(output_stream)
    writer.writerows(output_rows)
    return output_stream.getvalue()
if __name__ == '__main__':
    sample_csv = 'item,volume\napple,100\nbanana,200\ncherry,150'
    scale_factor = 2.5
    result = scale_volumes(sample_csv, scale_factor)
    print(result)