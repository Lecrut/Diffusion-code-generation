import datetime

class WeekdayCalculator:
    FULL_NAMES = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    @staticmethod
    def parse_date(date_str: str) -> datetime.date:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    @staticmethod
    def determine_weekday(date_str: str) -> str:
        date_obj = WeekdayCalculator.parse_date(date_str)
        return WeekdayCalculator.FULL_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    target = "2023-10-05"
    print(WeekdayCalculator.determine_weekday(target))