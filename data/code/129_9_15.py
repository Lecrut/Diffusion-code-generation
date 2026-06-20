from datetime import datetime

def filter_and_sort_events(events):
    today = datetime.now().date()
    return sorted(filter(lambda event: event.date() >= today, events), key=lambda event: event)

if __name__ == '__main__':
    sample_events = [
        datetime(2023, 10, 5),
        datetime(2023, 9, 28),
        datetime(2023, 10, 15),
        datetime(2023, 11, 1)
    ]
    print(filter_and_sort_events(sample_events))