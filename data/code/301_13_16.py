import datetime

class DateConverter:
    DATE_FORMAT_INPUT = '%Y-%m-%d'
    DATE_FORMAT_OUTPUT = '%d %B %Y'

    @staticmethod
    def convert_date(date_str: str) -> str:
        date_obj = datetime.datetime.strptime(date_str, DateConverter.DATE_FORMAT_INPUT)
        return date_obj.strftime(DateConverter.DATE_FORMAT_OUTPUT)

if __name__ == '__main__':
    sample_date = '2021-01-01'
    formatted_date = DateConverter.convert_date(sample_date)
    print(formatted_date)