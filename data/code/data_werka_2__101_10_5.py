import calendar

class DateAnalyzer:
    DAY_INDEX_MAP = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    @staticmethod
    def get_weekday_index(year: int, month: int, day: int) -> int:
        return calendar.weekday(year, month, day)

    @classmethod
    def get_day_name(cls, year: int, month: int, day: int) -> str:
        index = cls.get_weekday_index(year, month, day)
        return cls.DAY_INDEX_MAP[index]

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    result = DateAnalyzer.get_day_name(year, month, day)
    print(result)