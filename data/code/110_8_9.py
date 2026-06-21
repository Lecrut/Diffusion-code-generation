from datetime import date
from typing import List

class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event_date: date) -> None:
        if not isinstance(event_date, date):
            raise ValueError("Event must be a date object")
        self.events.append(event_date)

    def sort_events(self) -> List[date]:
        if not self.events:
            raise ValueError("No events to sort")
        sorted_events = sorted(self.events)
        self.events = []
        return sorted_events

if __name__ == '__main__':
    manager = EventManager()
    manager.add_event(date(2023, 12, 25))
    manager.add_event(date(2021, 1, 1))
    manager.add_event(date(2022, 7, 4))
    manager.add_event(date(2020, 10, 31))
    manager.add_event(date(2023, 1, 1))
    result = manager.sort_events()
    print(result)