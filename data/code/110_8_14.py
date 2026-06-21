from datetime import date

def sort_events(events):
    events.sort()
    return events

if __name__ == '__main__':
    event_dates = [
        date(2023, 12, 25),
        date(2021, 1, 1),
        date(2022, 7, 4),
        date(2023, 1, 1)
    ]
    sorted_dates = sort_events(event_dates)
    for d in sorted_dates:
        print(d)