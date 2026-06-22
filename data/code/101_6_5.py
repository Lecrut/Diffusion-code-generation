from dateutil.parser import parse

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

    @staticmethod
    def get_weekday(date_string: str) -> str:
        parsed = parse(date_string)
        return DateAnalyzer.WEEKDAY_MAP[parsed.weekday()]

if __name__ == '__main__':
    target = 'January 15, 2023'
    print(DateAnalyzer.get_weekday(target))