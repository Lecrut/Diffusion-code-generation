import calendar

class DateInfo:
    WEEKDAY_NAMES = list(calendar.day_name)

    @staticmethod
    def get_day_of_week(year, month, day):
        return DateInfo.WEEKDAY_NAMES[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    sample_date = (2023, 12, 25)
    print(f"The day of the week for {sample_date[1]}/{sample_date[0]} is {DateInfo.get_day_of_week(*sample_date)}.")