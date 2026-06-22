class DateChecker:
    _DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date_string: str):
        self.date_string = date_string
        self.year, self.month, self.day = self._parse_date(date_string)

    @staticmethod
    def _parse_date(date_string: str):
        if not isinstance(date_string, str):
            raise TypeError('Input must be a string')
        parts = date_string.split('-')
        if len(parts) != 3:
            raise ValueError('Date string must be in YYYY-MM-DD format')
        try:
            year, month, day = (int(parts[0]), int(parts[1]), int(parts[2]))
        except ValueError:
            raise ValueError('Date components must be integers')
        if not 1 <= month <= 12:
            raise ValueError('Invalid month')
        if day < 1:
            raise ValueError('Invalid day')
        days_in_month = list(DateChecker._DAYS_IN_MONTH)
        is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        if is_leap:
            days_in_month[2] = 29
        if day > days_in_month[month]:
            raise ValueError('Invalid day for given month and year')
        return (year, month, day)

    def _day_of_week(self):
        m = self.month
        y = self.year
        if m < 3:
            m += 12
            y -= 1
        q = self.day
        K = y % 100
        J = y // 100
        h = (q + 13 * (m + 1) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
        return (h + 5) % 7

    def is_weekday(self) -> bool:
        return self._day_of_week() < 5
if __name__ == '__main__':
    checker = DateChecker('2023-10-07')
    print(checker.is_weekday())
    checker2 = DateChecker('2023-10-08')
    print(checker2.is_weekday())
    checker3 = DateChecker('2024-02-29')
    print(checker3.is_weekday())
    checker4 = DateChecker('2023-02-28')
    print(checker4.is_weekday())
    try:
        DateChecker('2023-02-29')
    except ValueError:
        print('ValueError raised correctly for invalid date')