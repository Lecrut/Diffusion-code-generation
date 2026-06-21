from datetime import datetime

class DateFormatter:
    def __init__(self, reference_date=None):
        if reference_date is None:
            self.reference_date = datetime(2000, 1, 1)
        else:
            self.reference_date = reference_date

    def set_date(self, year, month, day):
        self.reference_date = datetime(year, month, day)

    def format_custom(self):
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        d = self.reference_date
        day_name = day_names[d.weekday()]
        month_name = month_names[d.month - 1]
        return f"{day_name}, {month_name} {d.day:02d}, {d.year}"

if __name__ == '__main__':
    formatter = DateFormatter()
    formatter.set_date(2023, 10, 25)
    print(formatter.format_custom())
    formatter.set_date(2000, 1, 1)
    print(formatter.format_custom())