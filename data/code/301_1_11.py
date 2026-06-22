from datetime import datetime

class DateFormatter:
    @staticmethod
    def convert_date(date_str):
        return datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%d')

if __name__ == '__main__':
    date_formatter = DateFormatter()
    sample_dates = ['10/27/2023', '01/01/2024', '12/31/2025']
    formatted_dates = [date_formatter.convert_date(date) for date in sample_dates]
    print(formatted_dates)