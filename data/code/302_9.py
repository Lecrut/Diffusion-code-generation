class DateCalculator:
    @staticmethod
    def get_day_number(year, month, day):
        import datetime
        date = datetime.date(year, month, day)
        return date.timetuple().tm_yday
if __name__ == '__main__':
    year = 2023
    month = 10
    day = 27
    day_number = DateCalculator.get_day_number(year, month, day)
    print(day_number)