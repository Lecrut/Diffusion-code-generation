from datetime import datetime

class DateComparator:
    def __init__(self, date_str1: str, date_str2: str):
        self.date_str1 = date_str1
        self.date_str2 = date_str2
        self.dt1 = self._validate_and_parse(date_str1)
        self.dt2 = self._validate_and_parse(date_str2)

    def _validate_and_parse(self, date_string: str) -> datetime:
        try:
            return datetime.fromisoformat(date_string)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid ISO 8601 date string: {date_string}") from e

    def get_earlier(self) -> datetime:
        return self.dt1 if self.dt1 < self.dt2 else self.dt2

if __name__ == '__main__':
    comparator = DateComparator("2024-05-20T10:00:00", "2024-05-20T12:00:00")
    result = comparator.get_earlier()
    print(result)