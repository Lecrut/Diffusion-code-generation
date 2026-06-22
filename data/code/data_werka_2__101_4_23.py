import calendar

class DateParser:
    def __init__(self, date_string: str):
        self.date_string = date_string
        self.year, self.month, self.day = map(int, date_string.split("-"))

    def get_day_of_week(self) -> int:
        return calendar.weekday(self.year, self.month, self.day)

if __name__ == '__main__':
    parser = DateParser("2023-10-23")
    print(parser.get_day_of_week())
    parser2 = DateParser("2024-01-01")
    print(parser2.get_day_of_week())
    parser3 = DateParser("2000-02-29")
    print(parser3.get_day_of_week())