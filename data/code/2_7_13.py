import csv
import io

def process_item_volumes(csv_content, scale_factor):
    input_stream = io.StringIO(csv_content)
    reader = csv.reader(input_stream)
    header = next(reader)
    
    results = []
    for row in reader:
        if len(row) >= 2:
            try:
                original_volume = float(row[1])
                scaled_volume = original_volume * scale_factor
                results.append([row[0], scaled_volume])
            except ValueError:
                results.append([row[0], 0.0])
    
    output_stream = io.StringIO()
    writer = csv.writer(output_stream)
    writer.writerow(header)
    for result_row in results:
        writer.writerow(result_row)
    
    return output_stream.getvalue()

if __name__ == '__main__':
    sample_csv = "Item,Volume\nBox A,10.5\nBox B,20.0\nBox C,5.5\n"
    scale = 2.5
    result = process_item_volumes(sample_csv, scale)
    print(result)