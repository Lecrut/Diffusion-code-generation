import json
import logging
from typing import Any, Dict, List
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler("item_counter.log")]
    )
def validate_item(item: Any) -> bool:
    return isinstance(item, (str, int)) and not isinstance(item, bool)
def count_items(data_list: List[Any]) -> Dict[str, int]:
    counts = {}
    logging.info(f"Processing data list of length {len(data_list)}")
    try:
        if not isinstance(data_list, list):
            raise TypeError("Input must be a list.")
        for idx, item in enumerate(data_list):
            if validate_item(item):
                counts[str(item)] = counts.get(str(item), 0) + 1
            else:
                logging.warning(f"Skipping invalid type at index {idx}: {type(item).__name__} - {item}")
        return counts
    except Exception as e:
        logging.error(f"Error processing items: {e}", exc_info=True)
        raise
def run_sample_test() -> None:
    setup_logging()
    sample_data = [
        "apple", 123, "banana", 
        {"key": "val"}, True, None, 
        456, "cherry", [], False, "date"
    ]
    try:
        result = count_items(sample_data)
        logging.info("Item counts generated successfully:")
        for item_str, count in sorted(result.items()):
            logging.debug(f"{item_str}: {count}")
    except Exception as e:
        logging.critical(f"Critical failure during sample test execution")
if __name__ == '__main__':
    run_sample_test()