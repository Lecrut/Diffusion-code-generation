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
        elapsed = end_time - self._start_time
        if elapsed < 0:
            raise ValueError("End time cannot be before the start time.")
        return elapsed
if __name__ == '__main__':
    tracker = TimeTracker()
    sample_start_time = None
    sample_end_time = None
    calculated_duration = None
    try:
        print("Starting time recording...")
        tracker.start()
        sample_start_time = tracker._start_time
        print(f"Start recorded at: {sample_start_time}")
        print("Simulating work for 2.5 seconds...")
        time.sleep(2.5)
        end_time = time.time()
        sample_end_time = end_time
        print(f"End time reached: {sample_end_time}")
        calculated_duration = tracker.duration(end_time)
        print(f"Calculated duration: {calculated_duration:.4f} seconds")
    except (ValueError, RuntimeError) as e:
        print(f"Error during operation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")