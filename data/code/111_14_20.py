from datetime import datetime

class DateTimeFormatter:
    def __init__(self):
        self.dt = datetime(2023, 10, 5, 14, 30, 0)

    def format_datetime(self):
        return self.dt.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    formatter = DateTimeFormatter()
    print(formatter.format_datetime())