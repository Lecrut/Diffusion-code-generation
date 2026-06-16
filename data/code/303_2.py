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
    print(f"Calculating elapsed time from first event (at time {time1}) to current time {time3}: {tracker.calculate_elapsed_time(time3)}")
    time4 = 100                                                        
    print(f"Calculating elapsed time from first event (at time {time1}) to time {time4}: {tracker.calculate_elapsed_time(time4)}")
    tracker2 = TimeTracker()
    time_a = 50
    print(f"\n--- Second Tracker Test ---")
    print(f"Recording event at time: {time_a}")
    tracker2.record_event(time_a)
    time_b = 150
    print(f"Calculating elapsed time from first event (at time {time_a}) to current time {time_b}: {tracker2.calculate_elapsed_time(time_b)}")