class TimeTracker:
    def __init__(self):
        self.first_event_time = None
    def record_event(self, timestamp):
        if self.first_event_time is None:
            self.first_event_time = timestamp
    def calculate_elapsed_time(self, current_timestamp):
        if self.first_event_time is None:
            return None
        return current_timestamp - self.first_event_time
if __name__ == '__main__':
    tracker = TimeTracker()
    time1 = 100
    print(f"Recording event at time: {time1}")
    tracker.record_event(time1)
    time2 = 350
    print(f"Recording event at time: {time2}")
    tracker.record_event(time2)
    current_time = 500
    elapsed = tracker.calculate_elapsed_time(current_time)
    print(f"Calculating elapsed time from first event to time {current_time}: {elapsed}")
    current_time_after_first = 150
    elapsed_after_first = tracker.calculate_elapsed_time(current_time_after_first)
    print(f"Calculating elapsed time from first event to time {current_time_after_first}: {elapsed_after_first}")
    no_events = TimeTracker()
    result_none = no_events.calculate_elapsed_time(100)
    print(f"Calculating elapsed time with no events: {result_none}")