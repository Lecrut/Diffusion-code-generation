import csv
import io
import tempfile

class VolumeProcessor:
    def __init__(self, input_data, scale_factor):
        self.input_data = input_data
        self.scale_factor = scale_factor

    def process(self):
        reader = csv.DictReader(io.StringIO(self.input_data))
        fieldnames = reader.fieldnames
        if not fieldnames:
            return io.StringIO()
        
        output_buffer = io.StringIO()
        writer = csv.DictWriter(output_buffer, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        
        for row in reader:
            if 'volume' not in row:
                continue
            try:
                volume = float(row['volume'])
                row['volume'] = volume * self.scale_factor
            except ValueError:
                continue
            writer.writerow(row)
        
        output_buffer.seek(0)
        return output_buffer.read()

if __name__ == '__main__':
    input_csv = "item_name,volume\nWidget,10.5\nGadget,20.0\nDoohickey,5.5"
    scaler = VolumeProcessor(input_csv, 2.5)
    result = scaler.process()
    print(result)