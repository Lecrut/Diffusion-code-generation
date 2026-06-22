import csv

class DateConverter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert_date_format(self):
        with open(self.input_file, 'r') as infile, open(self.output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                new_row = [self._convert_date(row[0]) if row[0] else None]
                writer.writerow(new_row)

    def _convert_date(self, date_str):
        month, day, year = map(int, date_str.split('/'))
        return f'{year:04d}-{month:02d}-{day:02d}'

if __name__ == '__main__':
    converter = DateConverter('input.csv', 'output.csv')
    converter.convert_date_format()