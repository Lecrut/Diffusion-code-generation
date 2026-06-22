import calendar

class DateVerifier:
    DAYS_IN_WEEK = 7

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def _validate_month(self):
        if not 1 <= self.month <= 12:
            raise ValueError("Month out of range")
        return self.month

    def _validate_day(self):
        max_days = calendar.monthrange(self.year, self.month)[1]
        if not 1 <= self.day <= max_days:
            raise ValueError("Day out of range")
        return self.day

    def get_day_of_month(self):
        self._validate_month()
        self._validate_day()
        return self.day

if __name__ == '__main__':
    verifier = DateVerifier(2024, 2, 29)
    print(verifier.get_day_of_month())