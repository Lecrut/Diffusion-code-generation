class DateDifferenceCalculator:
    @staticmethod
    def calculate_year_difference(date1: datetime, date2: datetime) -> int:
        return abs((date2.year - date1.year))

if __name__ == '__main__':
    from datetime import datetime
    date1 = datetime(2015, 7, 4)
    date2 = datetime(2030, 12, 25)
    difference = DateDifferenceCalculator.calculate_year_difference(date1, date2)
    print(difference)