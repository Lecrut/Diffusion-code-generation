import time
class TimeTracker:
    def __init__(self):
        self._start_time = None
    def start(self):
        if self._start_time is not None:
            raise ValueError("Time tracking has already started.")
        self._start_time = time.time()
    def stop(self):
        if self._start_time is None:
            raise RuntimeError("Time has not been started yet.")
        return time.time()
    def duration(self):
        if self._start_time is None:
            raise RuntimeError("No start time recorded.")
        end_time = time.time()
        return end_time - self._start_time
if __name__ == '__main__':
    tracker = TimeTracker()
    try:
        tracker.start()
        print("Time started.")
        time.sleep(2)
        end_time = tracker.stop()
        duration = tracker.duration()
        print(f"Time stopped at: {end_time}")
        print(f"Duration elapsed: {duration} seconds")
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")