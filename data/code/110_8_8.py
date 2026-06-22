from datetime import date

def sort_events(events):
    return sorted(events)

if __name__ == '__main__':
    events = [
        date(2023, 12, 25),
        date(2021, 1, 1),
        date(2022, 6, 15),
        date(2020, 9, 10),
        date(2024, 3, 1)
    ]
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)