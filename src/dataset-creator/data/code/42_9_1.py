import json
from datetime import datetime
from typing import List, Dict, Any
class SortManager:
    def __init__(self):
        self.log_file = "sort_operations.log"
        self.logger = None
    def initialize_logger(self) -> None:
        try:
            import logging
            if not logging.getLogger("SortManager").handlers:
                handler = logging.FileHandler(self.log_file, mode='w')
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                handler.setFormatter(formatter)
                logger_instance = logging.getLogger("SortManager")
                logger_instance.setLevel(logging.DEBUG)
                logger_instance.addHandler(handler)
            else:
                self.logger = logging.getLogger("SortManager")
        except Exception as e:
            error_msg = f"Failed to initialize logger with details: {str(e)}"
            print(error_msg)                                                               
    def log_operation(self, operation_name: str, data_type: type, success: bool, message: str) -> None:
        timestamp = datetime.now().isoformat()
        level = "INFO" if success else "ERROR"
        try:
            self.logger.log(level, f"[{timestamp}] [{operation_name}] {data_type.__name__}: {message}")
        except Exception as e:
            pass
    def sort_list(self, items: List[Any], key_func: Any = None) -> Dict[str, Any]:
        self.log_operation("sort_init", list, False, f"Processing {len(items)} items")
        if not isinstance(items, list):
            raise TypeError(f"Expected 'list' type but received '{type(items).__name__}' for input data.")
        if len(items) == 0:
            self.log_operation("sort_empty", int, True, "Input list was empty. Returning original structure.")
            return {
                "sorted_items": items,
                "original_count": 0,
                "error_message": None
            }
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                raise TypeError(f"Item at index {idx} is expected to be a dictionary but found '{type(item).__name__}'.")
        try:
            sorted_items = sorted(
                items, 
                key=lambda x: (x.get("key", ""), str(x)) if isinstance(key_func, type(lambda: None) and not callable(key_func)) else key_func(x),                                                                                                                   
            )
            self.log_operation("sort_complete", list, True, f"Successfully sorted {len(sorted_items)} items.")
        except TypeError as te:
            error_details = str(te)
            self.log_operation("sort_failed", type(te), False, f"Sorting failed due to invalid key or item structure: {error_details}")
            raise ValueError(f"Invalid sort configuration detected. Details: {error_details}") from te
    def process_sample_data(self) -> Dict[str, Any]:
        raw_data = [
            {"id": 102, "name": "Charlie", "score": 85},
            {"id": 101, "name": "Alice", "score": 92},
            {"id": 103, "name": "Bob", "score": 78}
        ]
        def get_name_key(item: Dict[str, Any]) -> str:
            return item.get("name", "").lower()
        manager = SortManager()
        try:
            manager.initialize_logger()
            result_data = manager.sort_list(raw_data, key_func=get_name_key)
            json_ready_output = {
                "status": "success",
                "message": f"Data sorted alphabetically by name.",
                "count": len(result_data["sorted_items"]),
                "items": result_data["sorted_items"]
            }
        except Exception as e:
            error_trace = str(e)
            return {
                "status": "error",
                "message": f"Unexpected exception occurred during processing.",
                "count": 0,
                "items": [],
                "exception_type": type(e).__name__,
                "traceback": error_trace[:200]                                             
            }
        return json_ready_output
if __name__ == '__main__':
    processor = SortManager()
    try:
        final_result = processor.process_sample_data()
        print(f"Processing Status: {final_result['status']}")
        if 'message' in final_result and not isinstance(final_result.get('exception_type'), str):
            print(f"Operation Result: {final_result['message']}")
    except Exception as e:
        error_msg = f"FATAL ERROR at script exit level. Details: {str(e)}"
        print(error_msg)