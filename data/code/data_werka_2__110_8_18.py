import datetime

def sort_events(events):
    return sorted(events)

if __name__ == '__main__':
    events = [
        datetime.date(2023, 12, 25),
        datetime.date(2023, 1, 1),
        datetime.date(2023, 6, 15),
        datetime.date(2023, 3, 10),
    ]
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)