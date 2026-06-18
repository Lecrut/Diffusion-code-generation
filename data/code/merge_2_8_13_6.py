import time
class StreamProcessor:
    def __init__(self):
        self.processed_count = 0
    def process_stream(self, data_source):
        for item in data_source:
            if isinstance(item, int) and item > 100:
                action_triggered = True
                while action_triggered:
                    print(f"Processing value {item}")
                    self.processed_count += 1
                    time.sleep(0.05)
                    break
    def run(self):
        sample_data = [45, 203, -10, 150, 99]
        start_time = time.time()
        for item in sample_data:
            if isinstance(item, int) and item > 100:
                print(f"Triggered action for {item}")
        elapsed = time.time() - start_time
        return self.processed_count
if __name__ == '__main__':
    processor = StreamProcessor()
    result = processor.run()
    print(f"Final processed count: {result}")