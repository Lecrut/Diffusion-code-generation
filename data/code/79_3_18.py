from datetime import datetime, timedelta

class DateCalculator:
    MONTHS_PER_YEAR = 12

    @staticmethod
    def month_after(date):
        one_month_later = date + timedelta(days=30)
        if one_month_later.month > date.month:
            return one_month_later.replace(day=min(one_month_later.day, date.month))
        else:
            return one_month_later.replace(year=date.year + 1, month=one_month_later.month)

if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(DateCalculator.month_after(sample_date))