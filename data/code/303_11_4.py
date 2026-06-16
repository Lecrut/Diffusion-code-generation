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
    def elapsed_time(self):
        if self._start_time is None:
            raise RuntimeError("No start time recorded yet.")
        current_time = time.time()
        return current_time - self._start_time
if __name__ == '__main__':
    tracker = TimeTracker()
    try:
        print("Starting time tracking...")
        tracker.start()
        print("Performing some work...")
        time.sleep(2)
        end_time = tracker.stop()
        duration = tracker.elapsed_time()
        print(f"Time tracking stopped.")
        print(f"Elapsed time: {duration} seconds")
        print("\nTesting error handling:")
        try:
            tracker.start()
        except ValueError as e:
            print(f"Caught expected error when starting twice: {e}")
        try:
            tracker.elapsed_time()
        except RuntimeError as e:
            print(f"Caught expected error when calculating before stopping: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")