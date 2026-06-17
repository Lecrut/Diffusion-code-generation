import sys
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('extractor_debug.log')
    ]
)
logger = logging.getLogger(__name__)
class FaultTolerantExtractor:
    def __init__(self):
        self.process_count = 0
        logger.info("FaultTolerantExtractor initialized")
    def extract_first(self, user_input_list):
        try:
            if not isinstance(user_input_list, (list, tuple)):
                raise TypeError(f"Expected list or tuple, got {type(user_input_list).__name__}")
            self.process_count += 1
            logger.debug(f"[Process #{self.process_count}] Received input of type {type(user_input_list).__name__} with length {len(user_input_list)}")
            if len(user_input_list) == 0:
                raise ValueError("Input list is empty. Cannot extract first element.")
            result = user_input_list[0]
            logger.debug(f"[Process #{self.process_count}] Successfully extracted value of type {type(result).__name__}: {result}")
            return result
        except Exception as e:
            error_msg = f"Error in extraction at process #{self.process_count}: {str(e)}"
            logger.error(error_msg, exc_info=True)
            if len(user_input_list) > 0 and not isinstance(result, (list, tuple)):
                return user_input_list[0]
            else:
                raise
def run_extraction_logic(sample_data):
    extractor = FaultTolerantExtractor()
    logger.info("Starting batch processing of sample data")
    for item in sample_data:
        try:
            first_elem = extractor.extract_first(item)
            print(f"Processed {item} -> Got {first_elem}")
        except Exception as e:
            logger.warning(f"Fallback triggered for {item}: {e}")
if __name__ == '__main__':
    SAMPLE_LISTS = [
        ["apple", "banana"],
        (10, 20, 30),
        [],
        {"key": "value"},
        [True],
        [42]
    ]
    run_extraction_logic(SAMPLE_LISTS)