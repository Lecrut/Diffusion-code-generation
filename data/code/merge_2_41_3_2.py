import json
import logging
from typing import Any, Dict, List
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
class ItemCounter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    def count_items(self, data_list: List[Any]) -> Dict[str, int]:
        if not isinstance(data_list, list):
            raise TypeError("Input must be a list.")
        result = {
            'strings': 0,
            'integers': 0,
            'objects': 0
        }
        for idx, item in enumerate(data_list):
            try:
                if isinstance(item, str) and not isinstance(item, (bytes, bytearray)):
                    result['strings'] += 1
                    self.logger.debug(f"String counted at index {idx}")
                elif isinstance(item, int) and not isinstance(item, bool):
                    result['integers'] += 1
                    self.logger.debug(f"Integer counted at index {idx}")
                else:
                    if item is None:
                        continue 
                    try:
                        json.dumps(item, default=str)
                        result['objects'] += 1
                        self.logger.debug(f"Object counted at index {idx}")
                    except TypeError as e:
                        result['objects'] += 1
                        self.logger.warning(f"Non-standard object counted at index {idx}: {type(item).__name__}")
            except Exception as e:
                self.logger.error(f"Error processing item at index {idx}: {e}", exc_info=True)
        return result
def run_sample():
    counter = ItemCounter()
    sample_data = [
        "apple", 123, {"key": "value"}, None, 
        "banana", -456, ["nested"], True, (1, 2), object(), {}
    ]
    try:
        counts = counter.count_items(sample_data)
        output_message = f"Counts: {counts}"
        logger.info(output_message)
        return counts
    except Exception as e:
        error_msg = f"Fatal Error during counting: {e}"
        logging.critical(error_msg, exc_info=True)
        raise
if __name__ == '__main__':
    setup_logging()
    try:
        result_counts = run_sample()
        print(f"Final Item Counts:\n{json.dumps(result_counts, indent=4)}")
    except Exception as e:
        logging.critical("Script execution failed", exc_info=True)