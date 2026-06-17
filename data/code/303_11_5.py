import time
class TimeTracker:
    def __init__(self):
        self._start_time = None
    def start(self):
        if self._start_time is None:
            self._start_time = time.time()
        else:
            raise RuntimeError("Start time has already been recorded.")
    def stop(self):
        if self._start_time is None:
            raise RuntimeError("No start time has been recorded yet.")
        return time.time()
    def duration(self, end_time):
        if self._start_time is None:
            raise RuntimeError("Start time must be recorded before calculating duration.")
        return end_time - self._start_time
if __name__ == '__main__':
    tracker = TimeTracker()
    try:
        print("Starting time recording...")
        tracker.start()
        print("Performing some work...")
        time.sleep(2)
        end_time = tracker.stop()
        print(f"Work finished at: {end_time}")
        duration = tracker.duration(end_time)
        print(f"Elapsed duration: {duration} seconds")
        try:
            tracker.duration(100)
        except RuntimeError as e:
            print(f"Error caught (Expected): {e}")
        try:
            tracker.stop()                                            
        except RuntimeError as e:
            print(f"Error caught (Expected): {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")