import calendar

WEEKDAY_INDEX_TO_NAME = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def determine_weekday(year, month, day):
    index = calendar.weekday(year, month, day)
    return WEEKDAY_INDEX_TO_NAME[index]

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_weekday_name(self):
        return determine_weekday(self.year, self.month, self.day)

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 12, 25)
    print(analyzer.get_weekday_name())