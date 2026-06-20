from datetime import date

class DateComparer:
    @staticmethod
    def are_dates_same(date1: date, date2: date) -> bool:
        if not isinstance(date1, date) or not isinstance(date2, date):
            raise TypeError('Both arguments must be instances of the date class')
        return date1 == date2

if __name__ == '__main__':
    try:
        print(DateComparer.are_dates_same(date(2023, 4, 1), date(2023, 4, 1)))
        print(DateComparer.are_dates_same(date(2023, 4, 1), date(2023, 4, 2)))
    except TypeError as e:
        print(e)