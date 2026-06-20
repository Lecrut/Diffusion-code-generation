from datetime import datetime

class DateTimeFormatter:
    def __init__(self):
        self.sample_date = datetime(2023, 10, 5, 14, 30, 0)

    def format_date(self):
        formatted_date = self.sample_date.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date

if __name__ == '__main__':
    formatter = DateTimeFormatter()
    print(formatter.format_date())