from datetime import datetime, timezone

class DateComparator:
    def __init__(self, date_str1: str, date_str2: str):
        self.date_str1 = date_str1
        self.date_str2 = date_str2
        self.dt1 = self._parse(date_str1)
        self.dt2 = self._parse(date_str2)

    @staticmethod
    def _parse(date_string: str) -> datetime:
        try:
            return datetime.fromisoformat(date_string)
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Invalid ISO 8601 format: {date_string}") from exc

    def get_earlier(self) -> str:
        if self.dt1 < self.dt2:
            return self.date_str1
        if self.dt2 < self.dt1:
            return self.date_str2
        return self.date_str1

    def get_later(self) -> str:
        if self.dt1 > self.dt2:
            return self.date_str1
        if self.dt2 > self.dt1:
            return self.date_str2
        return self.date_str1

if __name__ == '__main__':
    comparator = DateComparator("2024-05-10T14:30:00", "2024-05-10T14:30:00")
    earlier = comparator.get_earlier()
    later = comparator.get_later()
    print(earlier)
    print(later)