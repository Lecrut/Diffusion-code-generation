import csv

class DateFormatter:
    INPUT_FORMAT = '%m/%d/%Y'
    OUTPUT_FORMAT = '%Y-%m-%d'

    @staticmethod
    def format_date(date_str):
        return date_str.strftime(DateFormatter.OUTPUT_FORMAT)

    @classmethod
    def convert_dates(cls, input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                new_row = [cls.format_date(row[0]) if row[0] else None]
                writer.writerow(new_row)

if __name__ == '__main__':
    DateFormatter.convert_dates('input.csv', 'output.csv')