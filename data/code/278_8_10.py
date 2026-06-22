from datetime import datetime

class DateFormatter:
    DATE_FORMAT_INPUT = '%Y-%m-%d'
    DATE_FORMAT_OUTPUT = '%B %d, %Y'

    @staticmethod
    def format_date(date_str):
        try:
            date_obj = datetime.strptime(date_str, DateFormatter.DATE_FORMAT_INPUT)
            return date_obj.strftime(DateFormatter.DATE_FORMAT_OUTPUT)
        except ValueError:
            return f"Invalid date format: {date_str}"

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-12-25', '2024-07-04', 'invalid-date']
    formatter = DateFormatter()
    for date in sample_dates:
        print(formatter.format_date(date))