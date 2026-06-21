from datetime import date

def sort_events(events):
    events.sort()
    return events

if __name__ == '__main__':
    events = [
        date(2023, 10, 15),
        date(2021, 5, 1),
        date(2022, 12, 25),
        date(2020, 1, 1),
        date(2023, 1, 1)
    ]
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)