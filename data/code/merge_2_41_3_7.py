import json
import logging
from collections import Counter
from typing import Any, Dict, List
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
def validate_item(item: Any) -> bool:
    return isinstance(item, (str, int, float)) or hasattr(item, '__dict__')
def count_items(items: List[Any]) -> Dict[str, int]:
    counts = Counter()
    if not isinstance(items, list):
        raise TypeError("Input must be a list of items.")
    try:
        for idx, item in enumerate(items):
            is_valid = validate_item(item)
            if not is_valid and not hasattr(item, '__dict__'):
                logging.warning(f"Skipping unsupported type at index {idx}: {type(item).__name__}")
                continue
            item_key = str(item)
            counts[item_key] += 1
        if len(counts) > 0:
            logging.info(f"Processed {len(items)} items successfully. Found {sum(counts.values())} total entries.")
    except Exception as e:
        logging.error(f"Error processing item at index {idx}: {str(e)}")
        raise
    return dict(counts)
if __name__ == '__main__':
    setup_logging()
    sample_data = [
        "apple", 123, 
        {"key": "value"}, 
        "banana", 456.789,
        None,                                                          
        "cherry"
    ]
    try:
        result = count_items(sample_data)
        logging.info("Final Count Results:")
        print(json.dumps(result, indent=2))
    except (TypeError, ValueError) as e:
        logging.error(f"Fatal Error during processing: {e}")