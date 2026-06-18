import sys
from typing import List, Callable, Optional
class StreamProcessor:
    def __init__(self):
        self._active_criteria = []
    def add_condition(self, value: int, check_func: Callable[[int], bool]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric.")
        self._active_criteria.append({
            'value': value,
            'check_func': check_func
        })
    def process_stream(self, stream_data: List[int]) -> int:
        if not isinstance(stream_data, (list, tuple)):
            raise TypeError("Stream data must be iterable.")
        trigger_count = 0
        for item in stream_data:
            should_process = False
            for criterion in self._active_criteria:
                if isinstance(item, int) and abs(criterion['value'] - item) <= 1:
                    if criterion['check_func'](item):
                        should_process = True
                        break
            if should_process:
                trigger_count += 1
        return trigger_count
def main():
    raw_stream = [5, 6, 7, 8, 9]
    processor = StreamProcessor()
    def is_odd(x):
        return x % 2 == 1
    def is_even(x):
        return x % 2 == 0
    processor.add_condition(7, lambda x: True)
    processor.add_condition(9, is_odd)
    results = processor.process_stream(raw_stream)
    print(results)
if __name__ == '__main__':
    main()