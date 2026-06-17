import json
import logging
from collections import Counter
from typing import Any, Dict, List
def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
def count_items(data: Any, logger: logging.Logger) -> Dict[str, int]:
    try:
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")
        count_dict = Counter()
        for index, item in enumerate(data):
            try:
                normalized_item = str(item) if not isinstance(item, (int, float)) else f"{item}"
                count_dict[normalized_item] += 1
                logger.debug(f"Processed item at index {index}: type={type(item).__name__}, value='{normalized_item}'")
            except Exception as e:
                error_msg = f"Error processing item at index {index}: {str(e)}"
                logger.error(error_msg)
    except ValueError as ve:
        raise ve
    except TypeError as te:
        raise type(te)(f"Invalid data structure encountered.") from te
    return dict(count_dict)
def main():
    sample_data = [
        "apple", 10, {"key": "value"}, None, 
        "banana", "orange", 20.5, ["nested"], True, False
    ]
    logger = setup_logger("ItemCounter")
    try:
        result_counts = count_items(sample_data, logger)
        json_output = {str(k): v for k, v in result_counts.items()}
        print(json.dumps(json_output))
    except Exception as e:
        logger.critical(f"Application failed with error: {e}")
if __name__ == '__main__':
    main()