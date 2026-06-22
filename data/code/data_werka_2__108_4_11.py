import calendar

class DateVerifier:
    VALID_MONTHS = range(1, 13)
    MAX_DAYS = 31

    @staticmethod
    def _validate_month(month):
        if month not in DateVerifier.VALID_MONTHS:
            raise ValueError("Month must be between 1 and 12")
        return month

    @staticmethod
    def _validate_day(day):
        if day < 1 or day > DateVerifier.MAX_DAYS:
            raise ValueError("Day must be between 1 and 31")
        return day

    @staticmethod
    def verify_day(year, month, day):
        DateVerifier._validate_month(month)
        DateVerifier._validate_day(day)
        _, days_in_month = calendar.monthrange(year, month)
        if day > days_in_month:
            raise ValueError("Day is out of range for the given month")
        return day

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    verifier = DateVerifier()
    result = verifier.verify_day(year, month, day)
    print(result)