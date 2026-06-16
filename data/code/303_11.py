import time
class TimeTracker:
    def __init__(self):
        self._start_time = None
    def start(self):
        if self._start_time is None:
            self._start_time = time.time()
        else:
            raise ValueError("Start time has already been recorded.")
    def stop(self):
        if self._start_time is None:
            raise RuntimeError("No start time has been recorded yet.")
        return time.time()
    def duration(self, end_time):
        if self._start_time is None:
            raise RuntimeError("Start time must be recorded before calculating duration.")
        try:
            elapsed = end_time - self._start_time
            if elapsed < 0:
                raise ValueError("End time cannot be before the start time.")
            return elapsed
        except TypeError:
            raise TypeError("Invalid time values provided for duration calculation.")
if __name__ == '__main__':
    tracker = TimeTracker()
    start_time_val = 100.0
    end_time_val = 105.5
    try:
        tracker.start()
        print(f"Start time recorded.")
        actual_end_time = end_time_val 
        duration_result = tracker.duration(actual_end_time)
        print(f"Start time (internal reference): {tracker._start_time}")
        print(f"End time provided for calculation: {actual_end_time}")
        print(f"Calculated duration: {duration_result} seconds")
    except (ValueError, RuntimeError, TypeError) as e:
        print(f"Error occurred: {e}")