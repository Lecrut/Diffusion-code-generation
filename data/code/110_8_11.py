from datetime import datetime

class EventSorter:
    def __init__(self, events):
        self.events = events
    
    def sort_events(self):
        return sorted(self.events, key=lambda dt: (dt.year, dt.month, dt.day))
    
    def print_sorted_events(self):
        for event in self.sort_events():
            print(event)

if __name__ == '__main__':
    dates = [
        datetime(2023, 10, 25),
        datetime(2022, 5, 15),
        datetime(2023, 10, 1),
        datetime(2022, 1, 30),
        datetime(2023, 10, 25),
        datetime(2022, 5, 1),
    ]
    
    sorter = EventSorter(dates)
    sorter.print_sorted_events()