from datetime import date

def sort_events(events):
    events.sort()
    return events

if __name__ == '__main__':
    sample_dates = [date(2023, 1, 5), date(2022, 12, 25), date(2024, 1, 1)]
    sorted_dates = sort_events(sample_dates)
    print(sorted_dates)