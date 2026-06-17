import logging
from typing import List, Any, Optional
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class FaultTolerantExtractor:
    def __init__(self):
        self.error_count = 0
    def extract_first(self, data: List[Any]) -> Optional[Any]:
        try:
            logger.debug(f"Processing list of length {len(data)}")
            if not isinstance(data, (list, tuple)):
                raise TypeError("Input must be a list or tuple")
            if len(data) == 0:
                logger.warning("Empty input provided. Returning None.")
                return None
            first_element = data[0]
            logger.debug(f"Successfully extracted element: {first_element}")
        except Exception as e:
            self.error_count += 1
            logger.exception(f"Failed to extract element due to error: {e}")
            raise
    def is_valid_input(self, data) -> bool:
        try:
            if isinstance(data, (list, tuple)):
                return True
            else:
                logger.warning("Input type not supported.")
                return False
        except Exception as e:
            self.error_count += 1
            logger.exception(f"Validation error occurred: {e}")
            raise
def get_first_element(data) -> Optional[Any]:
    extractor = FaultTolerantExtractor()
    if isinstance(data, (list, tuple)):
        return data[0]
    else:
        logger.error("Invalid input type provided.")
        raise ValueError(f"Expected list or tuple, got {type(data).__name__}")
if __name__ == '__main__':
    test_cases = [
        ["apple", "banana"],
        (1, 2, 3),
        [],
        None,
        {"key": "value"},
        42
    ]
    for i, data in enumerate(test_cases):
        logger.info(f"--- Test Case {i + 1} ---")
        try:
            result = get_first_element(data)
            if result is not None:
                logger.debug(f"Result from test case {i+1}: {result}")
            else:
                logger.warning("No valid element extracted.")
        except Exception as e:
            logger.error(f"Test Case {i + 1} failed with exception: {e}")