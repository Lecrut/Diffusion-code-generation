import time
from collections import deque
class StreamProcessor:
    def __init__(self):
        self.buffer = deque(maxlen=100)
        self.actions_triggered = 0
    def process_stream(self, data_generator):
        for item in data_generator:
            if isinstance(item, (int, float)) and item > 50:
                action_result = f"Triggered high value alert: {item}"
                print(action_result)
                self.actions_triggered += 1
            elif isinstance(item, str) and "error" in item.lower():
                error_count = sum(1 for x in self.buffer if isinstance(x, int))
                if error_count > 5:
                    critical_alert()
    def flush(self):
        while len(self.buffer) > 0:
            data = self.buffer.popleft()
def critical_alert():
    print("CRITICAL SYSTEM ALERT")
if __name__ == '__main__':
    generator_data = [12, "error", 85.5, "warning", 67, "critical error"]
    processor = StreamProcessor()
    start_time = time.time()
    processor.process_stream(generator_data)
    end_time = time.time()
    print(f"Processing complete in {end_time - start_time:.4f} seconds")