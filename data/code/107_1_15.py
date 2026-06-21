from datetime import datetime

class DateConverter:
    def __init__(self, input_format, output_format):
        self.input_format = input_format
        self.output_format = output_format

    def convert(self, date_string):
        parsed = datetime.strptime(date_string, self.input_format)
        return parsed.strftime(self.output_format)

if __name__ == '__main__':
    converter = DateConverter('%m/%d/%Y', '%d-%m-%Y')
    sample_date = '07/04/2024'
    result = converter.convert(sample_date)
    print(result)