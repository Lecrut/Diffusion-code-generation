import logging
from typing import List, Tuple
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(funcName)s] - Message',
    datefmt='%Y-%m-%d %H:%M:%S'
)
def sort_keys_alphabetically(keys: List[str]) -> Tuple[List[str], str]:
    if not isinstance(keys, list):
        raise TypeError("Input must be a list of strings.")
    for index, key in enumerate(keys):
        if not isinstance(key, str):
            logging.error(f"Invalid entry at index {index}: Expected string, got {type(key).__name__}")
            raise TypeError(f"All elements must be strings. Invalid element found at index {index}.")
    sorted_keys = sorted(keys)
    logging.info(f"Successfully processed {len(sorted_keys)} keys.")
    return sorted_keys, "Keys have been successfully sorted alphabetically."
if __name__ == '__main__':
    sample_data: List[str] = ["zebra", "apple", "mango", "banana", "cherry"]
    try:
        logging.info("Starting alphabetical sort process.")
        sorted_result, message = sort_keys_alphabetically(sample_data)
        logging.info(f"Sorted keys: {sorted_result}")
        logging.debug(message)
        print(sorted_result)
    except (TypeError, ValueError) as e:
        logging.exception("An unexpected error occurred during key sorting.")
        raise