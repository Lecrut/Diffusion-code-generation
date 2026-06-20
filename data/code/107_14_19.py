from datetime import datetime

class DateFormatter:
    INPUT_FORMAT = '%d-%m-%Y %H:%M:%S'
    OUTPUT_FORMAT = '%Y-%m-%dT%H:%M:%S'

    @staticmethod
    def standardize_date_format(date_string):
        try:
            dt_object = datetime.strptime(date_string, DateFormatter.INPUT_FORMAT)
            return dt_object.strftime(DateFormatter.OUTPUT_FORMAT)
        except ValueError:
            return None

if __name__ == '__main__':
    date1 = '31-12-2023 23:59:59'
    print(f"Input: {date1}, Standardized: {DateFormatter.standardize_date_format(date1)}")