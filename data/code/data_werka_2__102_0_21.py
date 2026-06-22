import datetime

class DateValidator:
    def __init__(self, date_string: str):
        self.date_string = date_string
        self.parsed_date = None
        self._parse()

    def _parse(self):
        if not isinstance(self.date_string, str):
            raise ValueError("Input must be a string")
        if len(self.date_string) != 10:
            raise ValueError("Invalid date format: length mismatch")
        if self.date_string[4] != '-' or self.date_string[7] != '-':
            raise ValueError("Invalid date format: missing separators")
        try:
            year = int(self.date_string[0:4])
            month = int(self.date_string[5:7])
            day = int(self.date_string[8:10])
            self.parsed_date = datetime.date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid date format: {self.date_string}") from e

    def is_weekday(self) -> bool:
        if self.parsed_date is None:
            raise ValueError("Date not parsed")
        return self.parsed_date.weekday() < 5

    def get_weekday_name(self) -> str:
        if self.parsed_date is None:
            raise ValueError("Date not parsed")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[self.parsed_date.weekday()]

if __name__ == '__main__':
    test_cases = [
        "2023-10-07",
        "2023-10-08",
        "2023-02-29",
        "2023-13-01",
        "not-a-date"
    ]
    for date_str in test_cases:
        try:
            validator = DateValidator(date_str)
            is_weekday = validator.is_weekday()
            weekday_name = validator.get_weekday_name()
            print(f"{date_str}: is_weekday={is_weekday}, weekday={weekday_name}")
        except ValueError as e:
            print(f"{date_str}: Error - {e}")