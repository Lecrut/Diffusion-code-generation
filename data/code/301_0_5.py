from datetime import datetime

class DateFormatConverter:
    INPUT_FORMAT = '%Y-%m-%d'
    OUTPUT_FORMAT = '%d/%m/%Y'

    @staticmethod
    def convert_date_format(date_str):
        date_obj = datetime.strptime(date_str, DateFormatConverter.INPUT_FORMAT)
        return date_obj.strftime(DateFormatConverter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-12-31'
    converted_date = DateFormatConverter.convert_date_format(sample_date)
    print(converted_date)