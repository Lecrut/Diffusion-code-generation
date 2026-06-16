import time
from typing import List, Dict, Any
class DataProcessor:
    def __init__(self):
        self.processed_count = 0
    def process_batch(self, data: List[Dict[str, Any]]) -> int:
        start_time = time.perf_counter()
        try:
            result_data = []
            for item in data:
                if not isinstance(item.get('value'), (int, float)):
                    raise TypeError(f"Invalid value type for key 'value'")
                processed_item = {
                    "id": item["id"],
                    "processed_value": round(float(item["value"]) * 1.5, 2),
                    "status": "completed"
                }
                result_data.append(processed_item)
            self.processed_count += len(result_data)
        except Exception as e:
            print(f"Error during processing: {e}")
        end_time = time.perf_counter()
        duration_ms = (end_time - start_time) * 1000
        return {
            "success": True,
            "records_processed": len(result_data),
            "execution_time_ms": round(duration_ms, 2)
        }
def main():
    processor = DataProcessor()
    sample_dataset: List[Dict[str, Any]] = [
        {"id": 1001, "value": 45.6},
        {"id": 1002, "value": -123.89},
        {"id": 1003, "value": 789.0},
    ]
    try:
        result = processor.process_batch(sample_dataset)
        if not result["success"]:
            raise RuntimeError("Processing failed")
        print(f"Processed {result['records_processed']} records in {result['execution_time_ms']}ms")
        assert result['execution_time_ms'] < 10, "Performance benchmark exceeded: processing took too long."
    except Exception as e:
        print(f"FATAL ERROR: {e}")
if __name__ == '__main__':
    main()