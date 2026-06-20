import calendar

class WeekdayDeterminer:

    @staticmethod
    def get_weekday_name(year, month, day):
        date_obj = calendar.datetime.datetime(year, month, day)
        return date_obj.strftime('%A')
if __name__ == '__main__':
    determiner = WeekdayDeterminer()
    print(determiner.get_weekday_name(2023, 10, 26))
    print(determiner.get_weekday_name(2024, 1, 1))
    print(determiner.get_weekday_name(2025, 12, 31))