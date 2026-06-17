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
    time3 = 500
    print(f"Calculating elapsed time from first event to time: {time3}")
    elapsed1 = tracker.calculate_elapsed_time(time3)
    print(f"Elapsed time: {elapsed1}")
    time4 = 600
    print(f"Calculating elapsed time from first event to time: {time4}")
    elapsed2 = tracker.calculate_elapsed_time(time4)
    print(f"Elapsed time: {elapsed2}")