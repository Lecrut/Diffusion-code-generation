class TimeTracker:
    def __init__(self):
        self.first_event_time = None
        self.event_times = []
    def record_event(self, timestamp):
        if self.first_event_time is None:
            self.first_event_time = timestamp
        self.event_times.append(timestamp)
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
    time3 = 400
    tracker.record_event(time3)
    print(f"Recorded event at: {time3}")
    current_time = 500
    elapsed = tracker.calculate_elapsed_time(current_time)
    print(f"Current time: {current_time}")
    if elapsed is not None:
        print(f"Elapsed time since first event: {elapsed}")
    current_time_2 = 150
    elapsed_2 = tracker.calculate_elapsed_time(current_time_2)
    print(f"Current time: {current_time_2}")
    if elapsed_2 is not None:
        print(f"Elapsed time since first event: {elapsed_2}")