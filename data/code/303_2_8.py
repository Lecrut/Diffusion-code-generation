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
    tracker.record_event(time1)
    print(f"Recorded event at: {time1}")
    time2 = 350
    tracker.record_event(time2)
    print(f"Recorded event at: {time2}")
    time3 = 500
    elapsed1 = tracker.calculate_elapsed_time(time3)
    print(f"Elapsed time from first event to {time3}: {elapsed1}")
    time4 = 600
    elapsed2 = tracker.calculate_elapsed_time(time4)
    print(f"Elapsed time from first event to {time4}: {elapsed2}")