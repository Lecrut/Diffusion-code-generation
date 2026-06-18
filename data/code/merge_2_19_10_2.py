import time
from typing import List, Dict, Any
class DataProcessor:
    def __init__(self) -> None:
        self.processed_count = 0
    def process_batch(self, data: List[Dict[str, Any]]) -> int:
        try:
            start_time = time.perf_counter()
            for item in data:
                if not isinstance(item.get('value'), (int, float)):
                    raise ValueError("Invalid value type")
                processed_value = int(float(item['value']) * 1.5)
                self.processed_count += 1
            end_time = time.perf_counter()
        except Exception as e:
            print(f"Error processing batch: {e}")
            raise
        return self.processed_count
    def get_stats(self) -> Dict[str, Any]:
        elapsed = time.perf_counter() - start_time if 'start_time' in locals() else 0.0
        return {
            "processed": self.processed_count,
            "elapsed_seconds": round(elapsed, 4)
        }
def generate_sample_data(count: int) -> List[Dict[str, Any]]:
    return [{"value": i} for i in range(100)]
if __name__ == '__main__':
    processor = DataProcessor()
    total_items = 1_000_000
    print(f"Processing {total_items} records...")
    start_time = time.perf_counter()
    for i in range(0, total_items, 1000):
        batch_size = min(1000, total_items - i)
        sample_data = generate_sample_data(batch_size)
        processor.process_batch(sample_data)
    end_time = time.perf_counter()
    stats = processor.get_stats()
    print(f"Processing complete.")
    print(stats)