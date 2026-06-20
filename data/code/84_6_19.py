import calendar

class DateUtils:
    @staticmethod
    def get_day_number(year: int, month: int, day: int) -> int:
        return calendar.datetime.datetime(year, month, day).timetuple().tm_yday

if __name__ == '__main__':
    date_utils = DateUtils()
    print(date_utils.get_day_number(2023, 1, 1))
    print(date_utils.get_day_number(2024, 2, 29))
    print(date_utils.get_day_number(2024, 3, 1))