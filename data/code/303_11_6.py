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
            raise RuntimeError("Time tracking has not been started.")
        return time.time()
    def duration(self):
        if self._start_time is None:
            raise RuntimeError("No start time recorded yet.")
        end_time = time.time()
        return end_time - self._start_time
if __name__ == '__main__':
    tracker = TimeTracker()
    try:
        tracker.start()
        print("Start time recorded.")
        time.sleep(2)
        end_time = tracker.stop()
        duration = tracker.duration()
        print(f"End time recorded.")
        print(f"Elapsed duration: {duration} seconds")
    except (ValueError, RuntimeError) as e:
        print(f"Error during operation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")