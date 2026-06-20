from datetime import date

def sort_events(events):
    events.sort()
    return events

if __name__ == '__main__':
    sample_events = [date(2023, 1, 15), date(2022, 12, 25), date(2023, 3, 20)]
    sorted_events = sort_events(sample_events)
    print(sorted_events)