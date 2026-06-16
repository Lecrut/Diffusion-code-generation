class TimeTracker:
    def __init__(self):
        self._start_time = None
    def start(self, time):
        if time is not None:
            self._start_time = time
        else:
            raise ValueError("Start time cannot be None.")
    def stop(self, current_time):
        if self._start_time is None:
            raise RuntimeError("Time has not been started yet.")
        return current_time - self._start_time
if __name__ == '__main__':
    tracker = TimeTracker()
    sample_start = 100
    sample_end = 150
    try:
        tracker.start(sample_start)
        duration = tracker.stop(sample_end)
        print(f"Start time recorded: {sample_start}")
        print(f"End time provided: {sample_end}")
        print(f"Elapsed duration: {duration}")
        tracker_error = TimeTracker()
        try:
            tracker_error.stop(200)
        except RuntimeError as e:
            print(f"\nCaught expected error: {e}")
        try:
            tracker.start(None)
        except ValueError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")