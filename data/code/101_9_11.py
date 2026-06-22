import datetime

class DateAnalyzer:
    DAY_FORMAT = "%A"

    def __init__(self, date_string: str):
        self.date_string = date_string

    @staticmethod
    def _parse_date(date_string: str) -> datetime.datetime:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d")

    def get_day_of_week(self) -> str:
        parsed_date = self._parse_date(self.date_string)
        return parsed_date.strftime(self.DAY_FORMAT).upper()

if __name__ == '__main__':
    analyzer = DateAnalyzer("2023-11-11")
    result = analyzer.get_day_of_week()
    print(result)