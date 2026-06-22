import datetime

class CalendarHelper:
    DAY_MAP = {
        0: "MONDAY",
        1: "TUESDAY",
        2: "WEDNESDAY",
        3: "THURSDAY",
        4: "FRIDAY",
        5: "SATURDAY",
        6: "SUNDAY"
    }

    @staticmethod
    def get_weekday(year, month, day):
        date_obj = datetime.date(year, month, day)
        return CalendarHelper.DAY_MAP[date_obj.weekday()]

if __name__ == '__main__':
    result = CalendarHelper.get_weekday(2024, 7, 4)
    print(result)