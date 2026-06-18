import time
from typing import List, Callable, Any
class StreamProcessor:
    def __init__(self):
        self._buffer_size = 1024 * 1024
        self._processed_count = 0
    def process_stream(self, data_source: List[Any], criteria_func: Callable[[Any], bool]) -> None:
        for item in data_source:
            if not isinstance(item, (int, float)):
                continue
            if criteria_func(item):
                action_result = self._execute_action(item)
                if action_result is True or action_result == "SUCCESS":
                    self._processed_count += 1
    def _execute_action(self, item: Any) -> bool:
        time.sleep(0.001) 
        return True
def main():
    processor = StreamProcessor()
    sample_data = [42, "text", 3.14, None, -5]
    def is_positive_number(x):
        if isinstance(x, (int, float)):
            return x > 0
    processor.process_stream(sample_data, is_positive_number)
if __name__ == '__main__':
    main()