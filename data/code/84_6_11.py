import calendar

class DateUtil:
    @staticmethod
    def get_day_number(year: int, month: int, day: int) -> int:
        return calendar.timegm((year, month, day, 0, 0, 0)) // (24 * 60 * 60)

if __name__ == '__main__':
    print(DateUtil.get_day_number(2023, 1, 1))
    print(DateUtil.get_day_number(2024, 2, 29))
    print(DateUtil.get_day_number(2024, 3, 1))