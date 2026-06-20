from datetime import date

def sort_events(events):
    events.sort()
    return events

if __name__ == '__main__':
    events = [date(2023, 4, 1), date(2022, 1, 15), date(2023, 1, 1)]
    sorted_events = sort_events(events)
    print(sorted_events)