from datetime import datetime

def sort_dates(date_list):
    return sorted(date_list)

if __name__ == '__main__':
    event_dates = [
        datetime(2023, 11, 15),
        datetime(2022, 12, 25),
        datetime(2023, 10, 1),
        datetime(2022, 7, 4),
        datetime(2023, 11, 15),
        datetime(2022, 6, 1)
    ]
    sorted_events = sort_dates(event_dates)
    for date in sorted_events:
        print(date)