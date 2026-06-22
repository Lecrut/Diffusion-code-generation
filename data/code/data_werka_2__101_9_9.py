import datetime

class DateFormatter:
    def __init__(self, date_string):
        self.date_string = date_string

    def _parse(self):
        try:
            return datetime.datetime.strptime(self.date_string, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError(f"Invalid date format: {self.date_string}") from exc

    def get_day_upper(self):
        dt = self._parse()
        return dt.strftime("%A").upper()

if __name__ == '__main__':
    target = "2023-11-11"
    formatter = DateFormatter(target)
    result = formatter.get_day_upper()
    print(result)