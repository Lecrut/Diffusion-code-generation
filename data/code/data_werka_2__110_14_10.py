from datetime import date
from typing import List

def sort_timestamps_descending(timestamps: List[date]) -> List[date]:
    if not timestamps:
        return []
    return sorted(timestamps, key=lambda d: d.toordinal(), reverse=True)

if __name__ == '__main__':
    raw_timestamps = [
        date(2023, 1, 15),
        date(2021, 5, 20),
        date(2024, 12, 31),
        date(2022, 8, 10),
    ]
    result = sort_timestamps_descending(raw_timestamps)
    print(result)