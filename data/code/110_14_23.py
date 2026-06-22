from datetime import date
from typing import List

def sort_timestamps_descending(timestamps: List[date]) -> List[date]:
    reversed_list: List[date] = []
    current_index: int = len(timestamps)
    while current_index > 0:
        current_index -= 1
        reversed_list.append(timestamps[current_index])
    return sorted(reversed_list, reverse=True)

if __name__ == '__main__':
    input_dates: List[date] = [
        date(2023, 11, 5),
        date(2020, 2, 28),
        date(2024, 1, 1),
        date(2019, 7, 15),
    ]
    result: List[date] = sort_timestamps_descending(input_dates)
    print(result)