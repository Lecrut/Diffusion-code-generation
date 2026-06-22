from datetime import date

def sort_events(events):
    if not events:
        return []
    events.sort()
    return events

def format_dates(dates):
    return [d.isoformat() for d in dates]

if __name__ == '__main__':
    raw_events = [
        date(2023, 12, 25),
        date(2021, 1, 1),
        date(2022, 7, 4),
        date(2020, 10, 31),
        date(2023, 1, 1)
    ]
    sorted_events = sort_events(raw_events)
    formatted = format_dates(sorted_events)
    for item in formatted:
        print(item)