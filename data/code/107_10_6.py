from datetime import datetime

class DateFormatConverter:
    INPUT_FORMAT = '%Y-%m-%d'
    OUTPUT_FORMAT = '%d/%m/%Y'

    @staticmethod
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, DateFormatConverter.INPUT_FORMAT)
        return date_obj.strftime(DateFormatConverter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    converter = DateFormatConverter()
    formatted_date = converter.format_date(sample_date)
    print(formatted_date)