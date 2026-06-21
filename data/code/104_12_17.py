from datetime import datetime
from typing import Tuple

class DateComparator:
    SUPPORTED_FORMATS: Tuple[str, ...] = (
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%d %H:%M:%S",
    )

    @staticmethod
    def _parse(date_string: str) -> datetime:
        for fmt in DateComparator.SUPPORTED_FORMATS:
            try:
                return datetime.strptime(date_string, fmt)
            except ValueError:
                continue
        raise ValueError(f"Unsupported date format: {date_string}")

    @staticmethod
    def get_earlier(date_str1: str, date_str2: str) -> datetime:
        dt1 = DateComparator._parse(date_str1)
        dt2 = DateComparator._parse(date_str2)
        return dt1 if dt1 < dt2 else dt2

if __name__ == '__main__':
    result = DateComparator.get_earlier("2024-05-20T10:00:00", "2024-05-19T15:30:00")
    print(result)