import calendar

class DateFormatter:
    def __init__(self):
        self.month_names = {i: name for i, name in enumerate(calendar.month_name) if i > 0}

    def format_date_string(self, date_string):
        try:
            year, month, day = map(int, date_string.split('-'))
            return f"{self.month_names[month]} {day}, {year}"
        except ValueError:
            return "Invalid date format"

if __name__ == '__main__':
    formatter = DateFormatter()
    print(formatter.format_date_string("2023-10-05"))
    print(formatter.format_date_string("2024-01-31"))
    print(formatter.format_date_string("1999-12-01"))