from datetime import datetime

def filter_and_sort_events(event_list):
    today = datetime.today()
    return sorted(filter(lambda event: event > today, event_list))

if __name__ == '__main__':
    sample_events = [
        datetime(2023, 10, 5),
        datetime(2023, 9, 1),
        datetime(2024, 1, 15),
        datetime(2022, 12, 25)
    ]
    sorted_events = filter_and_sort_events(sample_events)
    print(sorted_events)