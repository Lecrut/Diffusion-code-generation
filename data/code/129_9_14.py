from datetime import datetime
TODAY = datetime.now().date()

def filter_and_sort_events(event_list):
    future_events = [event for event in event_list if event.date() >= TODAY]
    sorted_future_events = sorted(future_events)
    return sorted_future_events
if __name__ == '__main__':
    sample_events = [datetime(2023, 10, 5), datetime(2023, 9, 15), datetime(2024, 1, 1), datetime(2023, 8, 20)]
    filtered_sorted_events = filter_and_sort_events(sample_events)
    print(filtered_sorted_events)