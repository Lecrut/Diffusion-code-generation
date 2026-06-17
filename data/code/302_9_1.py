class DateCalculator:
    @staticmethod
    def get_day_number(year, month, day):
        import datetime
        date = datetime.date(year, month, day)
        return date.timetuple().tm_yday
if __name__ == '__main__':
    print(DateCalculator.get_day_number(2023, 10, 27))
    print(DateCalculator.get_day_number(2024, 1, 1))
    print(DateCalculator.get_day_number(1999, 12, 31))