import json
import logging
from typing import Any, Dict, List, Union
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
def calculate_item_counts(data: Any) -> Dict[str, int]:
    if not isinstance(data, list):
        logging.error("Input must be a list.")
        raise TypeError("Expected input to be a list.")
    result = {
        "string_count": 0,
        "int_count": 0,
        "object_count": 0,
        "total_items": len(data)
    }
    for index, item in enumerate(data):
        try:
            if isinstance(item, str):
                result["string_count"] += 1
                logging.debug(f"Index {index}: Processed string")
            elif isinstance(item, int):
                if not isinstance(item, bool):
                    result["int_count"] += 1
                    logging.debug(f"Index {index}: Processed integer")
                else:
                    logging.warning(f"Index {index}: Boolean found in list (counting as object)")
            elif hasattr(item, '__dict__') or not isinstance(item, (str, int)):
                result["object_count"] += 1
                logging.debug(f"Index {index}: Processed complex object")
            else:
                logging.warning(f"Index {index}: Unknown type encountered.")
        except Exception as e:
            logging.exception(f"Error processing item at index {index}")
            raise RuntimeError(f"Failed to process item at index {index} due to unexpected error.") from None
    return result
if __name__ == '__main__':
    sample_data = [
        "apple", 10, {"key": "value"}, True, "banana", 25.5, None, ["nested"], object()
    ]
    setup_logging()
    try:
        counts = calculate_item_counts(sample_data)
        print("Item Counts Report:")
        for key, value in counts.items():
            if isinstance(value, int):
                logging.info(f"{key}: {value}")
        json_output = json.dumps(counts, indent=2)
    except Exception as e:
        logging.critical("Fatal error in main execution")
        raise