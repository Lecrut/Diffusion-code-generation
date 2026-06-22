from datetime import date, timedelta

class YearSpanCalculator:
    FIRST_DAY = date(2023, 1, 1)
    LAST_DAY = date(2023, 12, 31)

    @staticmethod
    def calculate_span(start, end):
        delta = end - start
        return delta.days

    @classmethod
    def get_days_in_2023(cls):
        return cls.calculate_span(cls.FIRST_DAY, cls.LAST_DAY)

if __name__ == '__main__':
    result = YearSpanCalculator.get_days_in_2023()
    print(result)