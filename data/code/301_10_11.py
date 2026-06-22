import datetime

class DateFormatConverter:
    INPUT_FORMAT = '%Y-%m-%d'
    OUTPUT_FORMAT = '%d/%m/%Y'

    @staticmethod
    def convert_date_format(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, DateFormatConverter.INPUT_FORMAT)
            return date_obj.strftime(DateFormatConverter.OUTPUT_FORMAT)
        except ValueError:
            return "Error: Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    converter = DateFormatConverter()
    sample_date = "2023-10-27"
    converted_date = converter.convert_date_format(sample_date)
    print(converted_date)