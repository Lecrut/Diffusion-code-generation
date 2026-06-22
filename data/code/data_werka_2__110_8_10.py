from datetime import date
from typing import List

class EventCalendar:
    def __init__(self, name: str):
        self.name = name
        self._events: List[date] = []

    def add(self, d: date) -> None:
        self._events.append(d)

    def get_sorted(self) -> List[date]:
        return sorted(self._events)

    def count(self) -> int:
        return len(self._events)

if __name__ == '__main__':
    cal = EventCalendar("Q1_2024")
    cal.add(date(2024, 1, 15))
    cal.add(date(2024, 3, 31))
    cal.add(date(2024, 2, 14))
    cal.add(date(2024, 1, 1))
    cal.add(date(2024, 2, 29))

    sorted_list = cal.get_sorted()
    print(f"Calendar: {cal.name}")
    print(f"Total events: {cal.count()}")
    for d in sorted_list:
        print(d)