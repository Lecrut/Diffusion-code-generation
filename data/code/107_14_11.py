from datetime import datetime

class DateConverter:
    def __init__(self, input_format, output_format):
        self.input_format = input_format
        self.output_format = output_format

    def convert(self, date_string):
        parsed_date = datetime.strptime(date_string, self.input_format)
        return parsed_date.strftime(self.output_format)

if __name__ == '__main__':
    converter = DateConverter('%d-%m-%Y %H:%M:%S', '%Y-%m-%dT%H:%M:%S')
    sample_date = '25-12-2023 14:30:00'
    iso_date = converter.convert(sample_date)
    print(iso_date)
    print(converter.convert('01-01-2024 12:00:00'))