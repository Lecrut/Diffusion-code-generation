from datetime import datetime

class DateFormatConverter:
    INPUT_FORMAT = '%m/%d/%Y'
    OUTPUT_FORMAT = '%d-%m-%Y'

    @staticmethod
    def convert_date_format(date_string):
        try:
            date_object = datetime.strptime(date_string, DateFormatConverter.INPUT_FORMAT)
            return date_object.strftime(DateFormatConverter.OUTPUT_FORMAT)
        except ValueError:
            return "Invalid date format"

if __name__ == '__main__':
    converter = DateFormatConverter()
    print(converter.convert_date_format('12/31/2023'))
    print(converter.convert_date_format('01/01/2024'))
    print(converter.convert_date_format('25/08/1999'))