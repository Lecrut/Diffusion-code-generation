from datetime import datetime

class DateConverter:
    DATE_FORMAT_INPUT = '%d-%b-%Y'
    DATE_FORMAT_OUTPUT = '%Y%m%d'

    @staticmethod
    def convert_date_string(date_string):
        try:
            date_obj = datetime.strptime(date_string, DateConverter.DATE_FORMAT_INPUT)
            return date_obj.strftime(DateConverter.DATE_FORMAT_OUTPUT)
        except ValueError:
            return "Invalid Date Format"

if __name__ == '__main__':
    sample_date = '25-Jan-2023'
    print(f"'{sample_date}' converted: {DateConverter.convert_date_string(sample_date)}")