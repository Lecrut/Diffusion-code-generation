import calendar

class DateAnalyzer:
    DAY_MAP = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_weekday_name(self):
        index = calendar.weekday(self.year, self.month, self.day)
        return self.DAY_MAP[index]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 12, 25)
    print(analyzer.get_weekday_name())