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
def count_items(data: List[Any]) -> Dict[str, Any]:
    result = {
        'total': 0,
        'counts': {},
        'errors': []
    }
    logging.info("Starting item counting process")
    for idx, item in enumerate(data):
        try:
            if not validate_item(item):
                error_msg = f"Invalid type at index {idx}: {type(item).__name__}"
                result['errors'].append(error_msg)
                logging.warning(error_msg)
                continue
            current_type = type(item).__name__
            result['total'] += 1
            if current_type not in result['counts']:
                result['counts'][current_type] = 0
            result['counts'][current_type] += 1
        except Exception as e:
            error_msg = f"Unexpected exception at index {idx}: {str(e)}"
            result['errors'].append(error_msg)
            logging.error(error_msg, exc_info=True)
    if not result['total']:
        logging.warning("No valid items processed")
    return result
if __name__ == '__main__':
    setup_logging()
    sample_data = [
        "apple", 123, 45.67, {"key": "value"}, None, True, "banana"
    ]
    processed_data = []
    errors_found = False
    logging.info("Processing sample data")
    try:
        counts_result = count_items(sample_data)
        print(json.dumps(counts_result, indent=2))
        if not counts_result['errors']:
            logging.info(f"Successfully processed {counts_result['total']} items")
        else:
            for err in counts_result['errors']:
                logging.error(err)
    except Exception as e:
        logging.critical("Fatal error during execution", exc_info=True)