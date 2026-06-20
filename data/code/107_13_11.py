from datetime import datetime

class DateFormatter:
    DATE_INPUT_FORMAT = '%Y/%m/%d'
    DATE_OUTPUT_FORMAT = '%B %d, %Y'

    @staticmethod
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, DateFormatter.DATE_INPUT_FORMAT)
        return date_obj.strftime(DateFormatter.DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '2023/10/05'
    formatted_date = DateFormatter.format_date(sample_date)
    print(formatted_date)