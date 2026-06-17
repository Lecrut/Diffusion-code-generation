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
            raise ValueError("Time tracking has not been started yet.")
        return time.time()
    def duration(self):
        if self._start_time is None:
            raise ValueError("No start time recorded.")
        end_time = time.time()
        return end_time - self._start_time
if __name__ == '__main__':
    tracker = TimeTracker()
    try:
        tracker.start()
        print("Time tracking started.")
        time.sleep(2)
        end_time = tracker.stop()
        duration = tracker.duration()
        print(f"End time recorded: {end_time}")
        print(f"Elapsed duration: {duration:.4f} seconds")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")