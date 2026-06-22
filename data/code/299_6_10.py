from datetime import date

class WeekendAndHolidays:
    HOLIDAYS = [date(2023, 12, 25), date(2024, 1, 1)]
    
    @staticmethod
    def is_weekend(given_date):
        return given_date.weekday() >= 5
    
    @staticmethod
    def is_holiday(given_date):
        return given_date in WeekendAndHolidays.HOLIDAYS
    
    @classmethod
    def is_weekend_with_holidays(cls, given_date):
        return cls.is_weekend(given_date) or cls.is_holiday(given_date)

if __name__ == '__main__':
    sample_date = date(2023, 12, 26)
    print(WeekendAndHolidays.is_weekend_with_holidays(sample_date))