from datetime import datetime

class EventSorter:
    def __init__(self):
        self.today = datetime.now().date()

    def filter_and_sort_events(self, events):
        future_events = [event for event in events if event.date() > self.today]
        return sorted(future_events)

if __name__ == '__main__':
    sorter = EventSorter()
    sample_events = [
        datetime(2023, 10, 5),
        datetime(2023, 9, 28),
        datetime(2023, 11, 1),
        datetime(2023, 8, 25)
    ]
    sorted_events = sorter.filter_and_sort_events(sample_events)
    print(sorted_events)