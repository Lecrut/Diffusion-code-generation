from datetime import datetime, timezone
from typing import List

class ISODateSorter:
    STRPTIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def _parse_iso(date_str: str) -> datetime:
        return datetime.strptime(date_str, ISODateSorter.STRPTIME_FORMAT).replace(tzinfo=timezone.utc)

    @staticmethod
    def sort_dates(date_strings: List[str]) -> List[str]:
        if not date_strings:
            return []
        return sorted(date_strings, key=ISODateSorter._parse_iso)

if __name__ == '__main__':
    samples = [
        "2024-11-05T10:00:00",
        "2023-01-01T00:00:00",
        "2025-01-01T00:00:00",
        "2022-12-31T23:59:59"
    ]
    result = ISODateSorter.sort_dates(samples)
    print(result)