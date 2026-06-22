import calendar

class DateValidator:
    def __init__(self, date_string):
        if not isinstance(date_string, str):
            raise ValueError("Date must be a string")
        parts = date_string.split("-")
        if len(parts) != 3:
            raise ValueError("Date format must be YYYY-MM-DD")
        try:
            self.year = int(parts[0])
            self.month = int(parts[1])
            self.day = int(parts[2])
        except ValueError:
            raise ValueError("Date components must be integers")
        if not calendar.isleap(self.year) and self.month == 2 and self.day > 28:
            raise ValueError("Invalid day for month")
        if calendar.isleap(self.year) and self.month == 2 and self.day > 29:
            raise ValueError("Invalid day for month")
        if self.month < 1 or self.month > 12:
            raise ValueError("Invalid month")
        if self.day < 1 or self.day > calendar.monthrange(self.year, self.month)[1]:
            raise ValueError("Invalid day")

    def is_weekday(self):
        return calendar.weekday(self.year, self.month, self.day) < 5

if __name__ == "__main__":
    dates = ["2023-10-02", "2023-10-07", "2023-02-28"]
    for d in dates:
        validator = DateValidator(d)
        print(validator.is_weekday())