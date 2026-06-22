class DateParser:
    def __init__(self, date_string: str):
        parts = date_string.split("-")
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        self.year = int(parts[0])
        self.month = int(parts[1])
        self.day = int(parts[2])

    def is_leap_year(self, year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_days_in_month(self, year: int, month: int) -> int:
        days_map = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self.is_leap_year(year):
            return 29
        return days_map[month - 1]

    def validate(self) -> bool:
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1 or self.day > self.get_days_in_month(self.year, self.month):
            return False
        return True

    def calculate_day_of_week(self) -> int:
        if not self.validate():
            raise ValueError("Invalid date")
        total_days = 0
        for y in range(1, self.year):
            if self.is_leap_year(y):
                total_days += 366
            else:
                total_days += 365
        for m in range(1, self.month):
            total_days += self.get_days_in_month(self.year, m)
        total_days += self.day
        return (total_days - 1) % 7

if __name__ == '__main__':
    parser = DateParser("2023-10-23")
    print(parser.calculate_day_of_week())
    parser2 = DateParser("2024-01-01")
    print(parser2.calculate_day_of_week())
    parser3 = DateParser("2000-02-29")
    print(parser3.calculate_day_of_week())