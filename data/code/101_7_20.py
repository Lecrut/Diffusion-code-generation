import datetime

class DateAnalyzer:
    WEEKDAY_MAP = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_weekday_index(self):
        return self.date_obj.weekday()

    def get_weekday_name(self):
        index = self.get_weekday_index()
        return self.WEEKDAY_MAP[index]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2024, 7, 4)
    weekday_name = analyzer.get_weekday_name()
    print(weekday_name)