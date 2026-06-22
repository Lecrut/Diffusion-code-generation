from datetime import datetime

class DateFormatter:
    def __init__(self, input_format='%m/%d/%Y', output_format='%d-%m-%Y'):
        self.input_format = input_format
        self.output_format = output_format

    def convert(self, date_string):
        if not isinstance(date_string, str):
            raise TypeError("Date string must be a string")
        try:
            dt = datetime.strptime(date_string, self.input_format)
        except ValueError as e:
            raise ValueError(f"Cannot parse date '{date_string}' with format '{self.input_format}': {e}")
        return dt.strftime(self.output_format)

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_input = '01/15/2025'
    converted = formatter.convert(sample_input)
    print(converted)