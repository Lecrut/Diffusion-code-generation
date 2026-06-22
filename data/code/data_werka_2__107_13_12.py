import datetime

class DateFormatter:
    INPUT_FORMAT = '%Y/%m/%d'
    OUTPUT_FORMAT = '%B %d, %Y'

    @staticmethod
    def format_date(date_string: str) -> str:
        date_obj = datetime.datetime.strptime(date_string, DateFormatter.INPUT_FORMAT)
        return date_obj.strftime(DateFormatter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '2023/10/05'
    formatted = DateFormatter.format_date(sample_date)
    print(formatted)