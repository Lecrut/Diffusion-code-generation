from datetime import date

def sort_events(events):
    events_copy = list(events)
    events_copy.sort()
    return events_copy

if __name__ == '__main__':
    event_dates = [
        date(2024, 5, 12),
        date(2019, 11, 30),
        date(2022, 2, 14),
        date(2021, 8, 9),
        date(2023, 10, 31)
    ]
    chronological_events = sort_events(event_dates)
    for event_date in chronological_events:
        print(event_date)