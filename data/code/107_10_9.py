from datetime import datetime

class DateFormatter:
    INPUT_FORMAT = '%Y-%m-%d'
    OUTPUT_FORMAT = '%d/%m/%Y'

    @staticmethod
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, DateFormatter.INPUT_FORMAT)
        return date_obj.strftime(DateFormatter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    formatted_date = DateFormatter.format_date(sample_date)
    print(formatted_date)