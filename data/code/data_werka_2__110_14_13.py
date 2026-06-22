from datetime import date, datetime
from typing import List, Union
from collections import OrderedDict

DATE_FORMAT_MAP: OrderedDict[str, str] = OrderedDict([
    ("ISO", "%Y-%m-%d"),
    ("LONG", "%B %d, %Y"),
    ("SHORT", "%m/%d/%y")
])

class TimestampManager:
    def __init__(self, timestamps: List[Union[date, datetime]]) -> None:
        self.timestamps = list(timestamps)

    def sort_descending(self) -> List[Union[date, datetime]]:
        if not self.timestamps:
            return []
        valid_items = []
        for item in self.timestamps:
            if isinstance(item, (date, datetime)):
                valid_items.append(item)
            else:
                raise ValueError(f"Unsupported type: {type(item)}")
        return sorted(valid_items, reverse=True)

    def format_as(self, format_key: str) -> List[str]:
        fmt_str = DATE_FORMAT_MAP.get(format_key)
        if fmt_str is None:
            raise ValueError(f"Unknown format key: {format_key}")
        results = []
        for ts in self.sort_descending():
            if isinstance(ts, datetime):
                results.append(ts.strftime(fmt_str))
            else:
                results.append(ts.strftime(fmt_str))
        return results

if __name__ == '__main__':
    sample_timestamps = [
        date(2023, 1, 15),
        datetime(2021, 5, 20, 14, 30),
        date(2024, 12, 31),
        datetime(2022, 8, 10, 9, 0),
        date(2020, 2, 29),
    ]
    manager = TimestampManager(sample_timestamps)
    sorted_results = manager.sort_descending()
    print(sorted_results)
    formatted_results = manager.format_as("LONG")
    print(formatted_results)