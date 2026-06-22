class DateValidator:
    def __init__(self, date_string: str):
        if not isinstance(date_string, str):
            raise TypeError("Input must be a string")
        parts = date_string.split('-')
        if len(parts) != 3:
            raise ValueError("Date string must be in YYYY-MM-DD format")
        try:
            self.year = int(parts[0])
            self.month = int(parts[1])
            self.day = int(parts[2])
        except ValueError:
            raise ValueError('Date components must be integers')
        if self.year < 1 or self.month < 1 or self.month > 12 or self.day < 1:
            raise ValueError('Invalid date values')
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_leap = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
        if is_leap:
            days_in_month[2] = 29
        if self.day > days_in_month[self.month]:
            raise ValueError('Invalid day for given month and year')

    def is_weekday(self) -> bool:
        if self.year < 1000:
            raise ValueError("Year must be at least 1000")
        c = self.year // 100
        y = self.year % 100
        m = self.month
        d = self.day
        if m < 3:
            m += 12
            y -= 1
        h = (d + (13 * (m + 1)) // 5 + y + y // 4 + c // 4 - 2 * c) % 7
        return 0 <= h <= 4

if __name__ == '__main__':
    validator = DateValidator('2023-10-07')
    print(validator.is_weekday())
    validator2 = DateValidator('2023-10-08')
    print(validator2.is_weekday())
    validator3 = DateValidator('2024-02-29')
    print(validator3.is_weekday())