import time
from collections import deque
class StreamProcessor:
    def __init__(self):
        self.buffer = deque(maxlen=100)
        self.processed_count = 0
        self.triggered_actions = []
    def process_stream(self, data_generator):
        for item in data_generator:
            if isinstance(item, (int, float)) and item > 50:
                action_triggered = True
                self._execute_action(action_triggered)
                self.processed_count += 1
            else:
                continue
    def _execute_action(self, condition_met):
        timestamp = time.time()
        message = f"Action triggered at {timestamp} for value > 50"
        self.triggered_actions.append(message)
def generate_sample_data():
    yield 45.2
    yield 60.1
    yield -10
    yield 89.3
    yield 50.0
    yield 72.5
    yield "text"
    yield 95.8
if __name__ == '__main__':
    processor = StreamProcessor()
    data_source = generate_sample_data()
    start_time = time.time()
    processor.process_stream(data_source)
    end_time = time.time()
    print(f"Total items processed: {processor.processed_count}")
    for action in processor.triggered_actions:
        print(action)
    print(f"Processing completed in {(end_time - start_time):.4f} seconds")