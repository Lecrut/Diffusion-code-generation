from datetime import datetime

class DateFormatter:
    INPUT_FORMAT = '%m/%d/%Y'
    OUTPUT_FORMAT = '%Y-%m-%d'

    @staticmethod
    def format_date(date_str):
        return datetime.strptime(date_str, DateFormatter.INPUT_FORMAT).strftime(DateFormatter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_dates = ['10/27/2023', '01/01/2024', '12/31/2025']
    formatted_dates = [DateFormatter.format_date(date) for date in sample_dates]
    print(formatted_dates)