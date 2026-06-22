from datetime import datetime

class DateConverter:
    SOURCE_FORMAT = '%m/%d/%Y'
    TARGET_FORMAT = '%d-%m-%Y'

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, DateConverter.SOURCE_FORMAT)

    @staticmethod
    def format_date(parsed_date):
        return parsed_date.strftime(DateConverter.TARGET_FORMAT)

    @classmethod
    def convert(cls, date_string):
        parsed = cls.parse_date(date_string)
        return cls.format_date(parsed)

if __name__ == '__main__':
    sample_input = '02/28/2024'
    converter = DateConverter()
    converted_output = converter.convert(sample_input)
    print(converted_output)