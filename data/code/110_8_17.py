from datetime import date

def sort_events(events):
    events.sort()
    return events

if __name__ == '__main__':
    events = [
        date(2023, 12, 25),
        date(2021, 1, 1),
        date(2022, 7, 4),
        date(2020, 10, 31),
        date(2023, 1, 15)
    ]
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)