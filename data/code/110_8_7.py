import datetime

def sort_events(events):
    return sorted(events)

if __name__ == '__main__':
    events = [
        datetime.date(2023, 12, 25),
        datetime.date(2021, 1, 1),
        datetime.date(2022, 7, 4),
        datetime.date(2020, 10, 31),
    ]
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)