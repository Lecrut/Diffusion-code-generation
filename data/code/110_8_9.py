from datetime import date

def sort_events(events):
    events.sort()
    return events

if __name__ == '__main__':
    sample_dates = [date(2023, 4, 1), date(2022, 1, 15), date(2023, 2, 28)]
    sorted_dates = sort_events(sample_dates)
    print(sorted_dates)