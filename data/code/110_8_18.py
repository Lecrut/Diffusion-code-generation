from datetime import datetime

def sort_events(event_list):
    return sorted(event_list, key=lambda event: (event.year, event.month, event.day))

if __name__ == '__main__':
    events = [
        datetime(2023, 10, 25),
        datetime(2022, 5, 15),
        datetime(2023, 10, 1),
        datetime(2022, 1, 30),
        datetime(2023, 10, 25),
        datetime(2022, 5, 1),
    ]
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)