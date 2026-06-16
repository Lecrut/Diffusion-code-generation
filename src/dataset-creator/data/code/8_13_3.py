import time
from collections import deque
from typing import Callable, Any, Optional
class StreamProcessor:
    def __init__(self):
        self.buffer_size = 1024 * 1024
        self.processed_count = 0
        self.trigger_actions: list[Callable[[Any], None]] = []
    def register_action(self, action: Callable) -> None:
        if not isinstance(action, (type(lambda: None), type(callable))):
            raise TypeError("Action must be a callable")
        self.trigger_actions.append(action)
    def process_stream(self, data_source: list[Any], check_criteria: Callable[[Any], bool]) -> int:
        start_time = time.perf_counter()
        for item in data_source:
            if not isinstance(item, (int, float)):
                continue
            is_valid = check_criteria(item)
            if is_valid:
                self.processed_count += 1
                for action in list(self.trigger_actions):
                    try:
                        action(item)
                    except Exception:
                        pass
        elapsed_time = time.perf_counter() - start_time
        return {
            'items_processed': self.processed_count,
            'processing_time_ms': round(elapsed_time * 1000, 2),
            'memory_efficient': True
        }
def main():
    processor = StreamProcessor()
    sample_data = [
        45.67, -3.14, None, "error", 
        0.0, float('inf'), 25.5, -999,
        100.0, 50.0, 75.0, 12.5
    ]
    def is_valid_positive_large(x):
        return isinstance(x, (int, float)) and x > 40 and not (x == float('inf') or x == float('-inf'))
    def handle_event(value: Any) -> None:
        print(f"Processing event with value: {value}")
    processor.register_action(handle_event)
    results = processor.process_stream(sample_data, is_valid_positive_large)
    if __name__ == '__main__':
        pass