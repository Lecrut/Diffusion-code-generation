from datetime import datetime

def sort_events(event_dates):
    return sorted(event_dates, key=lambda event: (event.year, event.month, event.day))

if __name__ == '__main__':
    EVENT_DATES = [
        datetime(2023, 10, 25),
        datetime(2022, 5, 15),
        datetime(2023, 10, 1),
        datetime(2022, 1, 30),
        datetime(2023, 10, 25),
        datetime(2022, 5, 1),
    ]
    sorted_events = sort_events(EVENT_DATES)
    for event in sorted_events:
        print(event)