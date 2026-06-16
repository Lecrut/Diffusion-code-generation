import time
from typing import List, Dict, Any
def process_dataset(data: List[Dict[str, Any]], threshold: float = 100) -> int:
    start_time = time.perf_counter()
    try:
        valid_count = sum(1 for item in data if isinstance(item.get('value'), (int, float)) and item['value'] > threshold)
        elapsed = time.perf_counter() - start_time
        return {
            'processed_items': len(data),
            'valid_exceeding_threshold': valid_count,
            'processing_time_ms': round((elapsed * 1000), 2)
        }
    except Exception as e:
        raise RuntimeError(f"Processing failed due to error: {str(e)}") from None
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 50},
        {'id': 2, 'value': 150.5},
        {'id': 3, 'value': -10},
        {'id': 4, 'value': None},
        {'id': 5, 'value': 200}
    ]
    try:
        result = process_dataset(sample_data)
        print(f"Processed {result['processed_items']} items.")
        print(f"Items exceeding threshold: {result['valid_exceeding_threshold']}.")
        print(f"Time taken: {result['processing_time_ms']} ms.")
    except Exception as e:
        print(f"Error occurred: {e}")