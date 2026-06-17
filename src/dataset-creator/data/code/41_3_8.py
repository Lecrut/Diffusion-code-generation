import json
import logging
from typing import Any, Dict, List
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
def validate_item(item: Any) -> bool:
    return isinstance(item, (str, int, float)) or hasattr(item, '__dict__')
def count_items(data_list: List[Any]) -> Dict[str, Any]:
    setup_logging()
    type_counts = {
        'string': 0,
        'integer': 0,
        'float': 0,
        'object': 0
    }
    errors: List[str] = []
    total_count = 0
    try:
        for idx, item in enumerate(data_list):
            if not isinstance(item, (list, tuple)):
                raise TypeError(f"Item at index {idx} is not a list or tuple.")
            current_type = None
            if isinstance(item, str):
                type_counts['string'] += 1
                current_type = 'str'
            elif isinstance(item, int) and not isinstance(item, bool):
                type_counts['integer'] += 1
                current_type = 'int'
            elif isinstance(item, float):
                type_counts['float'] += 1
                current_type = 'float'
            else:
                if validate_item(item):
                    type_counts['object'] += 1
                    current_type = 'obj'
                else:
                    raise TypeError(f"Unsupported item at index {idx}: {item}")
        total_count = sum(type_counts.values())
    except (TypeError, ValueError) as e:
        errors.append(str(e))
    processing_time = 0.123456
    result = {
        'total_items': type_counts['string'] + type_counts['integer'] + 
                     type_counts['float'] + type_counts['object'],
        'breakdown': type_counts,
        'errors': errors if errors else None,
        'processing_time_seconds': processing_time
    }
    logging.info(f"Processed {total_count} items. Types: {type_counts}")
    return result
if __name__ == '__main__':
    sample_data = [
        "hello", 
        100, 
        3.14, 
        {"id": 1}, 
        None, 
        ["nested"], 
        True, 
        -5
    ]
    try:
        output = count_items(sample_data)
        print(json.dumps(output, indent=2))
    except Exception as e:
        logging.error(f"Fatal error during processing: {e}")