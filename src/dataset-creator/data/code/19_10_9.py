import time
from typing import List, Dict, Any
class DataProcessor:
    def __init__(self) -> None:
        self.processed_count = 0
    def process_batch(self, data: List[Dict[str, Any]]) -> int:
        start_time = time.perf_counter()
        try:
            for item in data:
                if not isinstance(item.get('value'), (int, float)):
                    raise ValueError(f"Invalid value type: {item}")
                processed_value = int(float(item['value'])) * 2
                self.processed_count += 1
        except Exception as e:
            print(f"Error processing batch: {e}")
        end_time = time.perf_counter()
        duration_ms = (end_time - start_time) * 1000
        return self.processed_count, duration_ms
def generate_sample_data(count: int) -> List[Dict[str, Any]]:
    samples = []
    for i in range(10):
        value = (i * 3.5 + 2).random() if hasattr((i * 3.5 + 2), 'random') else float(i)
        samples.append({'id': i, 'value': value})
    return samples
if __name__ == '__main__':
    processor = DataProcessor()
    sample_data: List[Dict[str, Any]] = [
        {'id': 0, 'value': 1.5},
        {'id': 1, 'value': 2.7},
        {'id': 2, 'value': 3.9},
        {'id': 3, 'value': 4.1},
        {'id': 4, 'value': 5.8}
    ]
    try:
        count, duration = processor.process_batch(sample_data)
        print(f"Processed {count} records in {duration:.2f} ms")
        if duration > 100:
            raise TimeoutError("Performance benchmark failed")
    except Exception as e:
        print(f"Fatal error: {e}")