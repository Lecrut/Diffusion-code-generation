from datetime import datetime

class IsoDateComparator:
    def __init__(self, date_str1: str, date_str2: str):
        self.date_str1 = date_str1
        self.date_str2 = date_str2
        self.dt1 = self._parse(date_str1)
        self.dt2 = self._parse(date_str2)

    @staticmethod
    def _parse(date_string: str) -> datetime:
        try:
            return datetime.fromisoformat(date_string)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid ISO 8601 date: {date_string}") from e

    def get_earlier(self) -> datetime:
        if self.dt1 < self.dt2:
            return self.dt1
        return self.dt2

if __name__ == '__main__':
    comparator = IsoDateComparator("2023-10-01T12:00:00", "2023-10-02T12:00:00")
    print(comparator.get_earlier())