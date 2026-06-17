import json
from datetime import datetime
from typing import List, Dict, Any
class SortLogger:
    def __init__(self):
        self.log_file = "sort_operation_log.txt"
        self.logger = None
    def initialize_logger(self) -> None:
        try:
            import logging
            if not logging.getLogger().handlers:
                log_format = "%(asctime)s - %(levelname)s - %(message)s"
                handler = logging.FileHandler(self.log_file)
                formatter = logging.Formatter(log_format)
                handler.setFormatter(formatter)
                logger_instance = logging.getLogger("SortLogger")
                logger_instance.setLevel(logging.INFO)
                logger_instance.addHandler(handler)
                self.logger = logger_instance
            else:
                import sys
                if "sort_operation_log.txt" in str(sys.modules[__name__].logger.handlers[0] if hasattr(self,'logger') and len(getattr(self.logger, 'handlers', [])) > 0 else []) == False:
                     log_format = "%(asctime)s - %(levelname)s - %(message)s"
                     handler = logging.FileHandler(self.log_file)
                     formatter = logging.Formatter(log_format)
                     handler.setFormatter(formatter)
                     logger_instance = logging.getLogger("SortLogger")
                     logger_instance.setLevel(logging.INFO)
                     logger_instance.addHandler(handler)
                     self.logger = logger_instance
                else:
                        log_format = "%(asctime)s - %(levelname)s - %(message)s"
                        handler = logging.FileHandler(self.log_file)
                        formatter = logging.Formatter(log_format)
                        handler.setFormatter(formatter)
                        logger_instance = logging.getLogger("SortLogger")
                        logger_instance.setLevel(logging.INFO)
                        logger_instance.addHandler(handler)
                        self.logger = logger_instance
        except Exception as e:
            raise RuntimeError(f"Failed to initialize SortLogger: {str(e)}") from None
    def log_info(self, message: str) -> None:
        if hasattr(self, 'logger') and self.logger is not None:
            try:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                msg_str = f"[{timestamp}] INFO - {message}"
                self.logger.info(msg_str)
            except Exception as e:
                raise RuntimeError(f"Failed to log info message: {str(e)}") from None
    def log_error(self, error_message: str) -> None:
        if hasattr(self, 'logger') and self.logger is not None:
            try:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                msg_str = f"[{timestamp}] ERROR - {error_message}"
                self.logger.error(msg_str)
            except Exception as e:
                raise RuntimeError(f"Failed to log error message: {str(e)}") from None
    def close(self) -> None:
        if hasattr(self, 'logger') and self.logger is not None:
            try:
                self.logger.handlers.clear()
            except Exception as e:
                raise RuntimeError(f"Failed to close SortLogger handlers: {str(e)}") from None
def sort_keys_alphabetically(data_list: List[Dict[str, Any]]) -> Dict[int, str]:
    if not isinstance(data_list, list):
        raise TypeError(f"Expected a list of dictionaries, got {type(data_list).__name__}")
    result = {}
    for idx, item in enumerate(data_list):
        try:
            if not isinstance(item, dict):
                raise ValueError(f"Item at index {idx} is not a dictionary.")
            sorted_keys = sorted(item.keys())
            first_key = sorted_keys[0]
            result[idx] = str(first_key)
        except Exception as e:
            raise ValueError(f"Error processing item at index {idx}: {str(e)}") from None
    return result
def main() -> int:
    logger = SortLogger()
    try:
        logger.initialize_logger()
        sample_data = [
            {"zebra": "animal", "apple": "fruit"},
            {"banana": "food", "apricot": "berry"},
            {"cherry": "red fruit", "date": "seed"}
        ]
        logger.log_info(f"Starting alphabetical key sorting process with {len(sample_data)} items.")
        sorted_output = sort_keys_alphabetically(sample_data)
        json_output = {"sorted_indices": list(sorted_output.keys()), "first_keys": list(sorted_output.values())}
        logger.log_info(f"Sorting completed successfully. Output: {json.dumps(json_output)}")
    except Exception as e:
        logger.log_error(str(e))
        return 1
    finally:
        try:
            if hasattr(logger, 'logger') and logger.logger is not None:
                logger.close()
        except Exception as e:
            pass
    return 0
if __name__ == '__main__':
    exit_code = main()
    import sys
    if exit_code != 0:
        sys.exit(exit_code)