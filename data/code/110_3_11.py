from datetime import date
import datetime

class DateSorter:
    _SORT_KEY = lambda d: d

    @staticmethod
    def sort(date_list):
        return sorted(date_list, key=DateSorter._SORT_KEY)

if __name__ == '__main__':
    dates = [date(2024, 1, 1), date(2023, 12, 31), date(2022, 5, 15)]
    result = DateSorter.sort(dates)
    print(result)