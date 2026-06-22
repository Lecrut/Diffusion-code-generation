from datetime import datetime

class DateFormatter:
    INPUT_FORMAT = '%Y-%m-%d'
    OUTPUT_FORMAT = '%d/%m/%Y'

    @staticmethod
    def convert_date_format(date_str):
        date_obj = datetime.strptime(date_str, DateFormatter.INPUT_FORMAT)
        return date_obj.strftime(DateFormatter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    converted_date = DateFormatter.convert_date_format(sample_date)
    print(converted_date)