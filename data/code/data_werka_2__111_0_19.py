from datetime import date

class YearDayCounter:
    START_DATE = date(2023, 1, 1)
    END_DATE = date(2023, 12, 31)

    @staticmethod
    def calculate_span():
        delta = YearDayCounter.END_DATE - YearDayCounter.START_DATE
        return delta.days

if __name__ == '__main__':
    days = YearDayCounter.calculate_span()
    print(days)