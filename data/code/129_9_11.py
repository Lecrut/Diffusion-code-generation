from datetime import datetime

def filter_and_sort_events(events):
    today = datetime.now().date()
    future_events = [event for event in events if event.date() >= today]
    return sorted(future_events, key=lambda x: x)

if __name__ == '__main__':
    sample_events = [
        datetime(2023, 10, 5),
        datetime(2023, 9, 15),
        datetime(2024, 1, 1),
        datetime(2022, 12, 25)
    ]
    sorted_events = filter_and_sort_events(sample_events)
    print(sorted_events)