import datetime

class YearCalculator:
    SECONDS_PER_DAY = 24 * 60 * 60
    
    @staticmethod
    def calculate_total_seconds_in_year():
        year_start = datetime.date(datetime.datetime.now().year, 1, 1)
        year_end = datetime.date(datetime.datetime.now().year + 1, 1, 1)
        delta = year_end - year_start
        return delta.days * YearCalculator.SECONDS_PER_DAY

if __name__ == '__main__':
    total_seconds = YearCalculator.calculate_total_seconds_in_year()
    print(total_seconds)