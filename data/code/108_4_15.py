import calendar

class DateVerifier:
    VALID_MONTHS = range(1, 13)
    VALID_DAYS_RANGE = range(1, 32)

    @staticmethod
    def _get_max_days(year, month):
        return calendar.monthrange(year, month)[1]

    def verify_day(self, year, month, day):
        if month not in self.VALID_MONTHS:
            raise ValueError("Invalid month")
        if day not in self.VALID_DAYS_RANGE:
            raise ValueError("Invalid day")
        max_days = self._get_max_days(year, month)
        if day > max_days:
            raise ValueError("Day out of range")
        return day

if __name__ == '__main__':
    verifier = DateVerifier()
    year = 2024
    month = 2
    day = 29
    result = verifier.verify_day(year, month, day)
    print(result)