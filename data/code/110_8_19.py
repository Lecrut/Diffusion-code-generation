from datetime import datetime

def sort_events(event_dates):
    return sorted(event_dates, key=lambda event: (event.year, event.month, event.day))

if __name__ == '__main__':
    events = [
        datetime(2023, 11, 5),
        datetime(2022, 9, 20),
        datetime(2023, 11, 5),
        datetime(2022, 8, 10),
        datetime(2023, 12, 15),
        datetime(2022, 7, 5)
    ]
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)