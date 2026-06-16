import time
class TimeTracker:
    def __init__(self):
        self._start_time = None
    def start(self):
        if self._start_time is not None:
            raise ValueError("Time tracking has already started. Please stop before starting again.")
        self._start_time = time.time()
    def stop(self):
        if self._start_time is None:
            raise RuntimeError("Time tracking has not been started yet.")
        self._start_time = None
    def duration(self):
        if self._start_time is None:
            raise RuntimeError("No start time recorded. Please start the timer first.")
        elapsed = time.time() - self._start_time
        return elapsed
if __name__ == '__main__':
    tracker = TimeTracker()
    try:
        print("Starting time tracking...")
        tracker.start()
        print("Working for a short period...")
        time.sleep(2)
        duration_seconds = tracker.duration()
        print(f"Elapsed time: {duration_seconds:.4f} seconds")
        print("Stopping time tracking.")
        tracker.stop()
        print("Attempting to calculate duration after stopping (should fail):")
        try:
            tracker.duration()
        except RuntimeError as e:
            print(f"Caught expected error: {e}")
        print("Attempting to start again (should fail):")
        try:
            tracker.start()
        except ValueError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during the main execution: {e}")