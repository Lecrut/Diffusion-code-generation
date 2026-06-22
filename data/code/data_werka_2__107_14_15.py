from datetime import datetime

class DateConverter:
    def __init__(self, input_format: str, output_format: str):
        self.input_format = input_format
        self.output_format = output_format

    def convert(self, date_string: str) -> str:
        parsed_date = datetime.strptime(date_string, self.input_format)
        return parsed_date.strftime(self.output_format)

    def get_format_info(self) -> dict:
        return {
            'input': self.input_format,
            'output': self.output_format
        }

if __name__ == '__main__':
    converter = DateConverter('%d-%m-%Y %H:%M:%S', '%Y-%m-%dT%H:%M:%S')
    sample_date = '15-08-2023 09:15:30'
    iso_date = converter.convert(sample_date)
    print(iso_date)
    print(converter.get_format_info())