import sys
from typing import List, Callable, Any
class StreamProcessor:
    def __init__(self):
        self._buffer_size = 1024 * 1024
    def process(self, data_stream: List[Any], criteria_func: Callable[[Any], bool]) -> None:
        for item in data_stream:
            if not isinstance(item, (int, float)):
                continue
            if criteria_func(item):
                self._trigger_action(item)
    def _trigger_action(self, value: Any) -> None:
        print(f"Action triggered for {value}")
if __name__ == '__main__':
    sample_data = [10.5, 20.3, "text", 30.7, -45.9]
    def is_positive(value):
        return value > 0
    processor = StreamProcessor()
    processor.process(sample_data, is_positive)