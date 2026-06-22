import datetime

class DateFormatter:
    DATE_FORMAT_INPUT = '%Y-%m-%d'
    DATE_FORMAT_OUTPUT = '%d %B %Y'

    @staticmethod
    def format_date(date_str: str) -> str:
        return datetime.datetime.strptime(date_str, DateFormatter.DATE_FORMAT_INPUT).strftime(DateFormatter.DATE_FORMAT_OUTPUT)

if __name__ == '__main__':
    sample_date = '2021-01-01'
    formatted_date = DateFormatter.format_date(sample_date)
    print(formatted_date)