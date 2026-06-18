import json
import logging
from typing import Any, Dict, List, Union
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(funcName)s] - %(message)s'
)
logger = logging.getLogger(__name__)
class ItemPresenceChecker:
    def __init__(self):
        self.check_history: List[Dict[str, Any]] = []
    def check_presence(self, target_value: Any, data_sources: Dict[str, Union[List[Any], str]]) -> bool:
        logger.info(f"Starting search for target value: {target_value}")
        normalized_sources = []
        for source_name, content in data_sources.items():
            if isinstance(content, str):
                try:
                    parsed_content = json.loads(content)
                    logger.debug(f"Parsed string '{source_name}' as JSON")
                except json.JSONDecodeError:
                    import ast
                    if content.startswith('['):
                        parsed_content = ast.literal_eval(content)
                        logger.debug(f"Parsed string '{source_name}' as literal")
                    else:
                        normalized_sources.append((source_name, [content]))
                        continue
            elif isinstance(content, list):
                try:
                    parsed_content = json.loads(json.dumps(content))
                except TypeError:
                    pass
                normalized_sources.append((source_name, content))
        found_in_source = None
        if not normalized_sources:
            logger.warning("No valid data sources provided.")
            return False
        for source_name, items in normalized_sources:
            is_present = target_value in items
            if is_present:
                found_in_source = source_name
                logger.info(f"Item '{target_value}' found at {source_name}")
        return bool(found_in_source)
    def log_check_result(self, target_value: Any, result: bool):
        status_msg = "FOUND" if result else "NOT FOUND"
        logger.info(f"[RESULT] Target '{target_value}': {status_msg}")
def run_main():
    target_item = 42
    sources_data: Dict[str, Union[List[Any], str]] = {
        "numeric_list": [10, 20, 30, 42, 50],
        "string_array_json": json.dumps(["apple", "banana", "cherry"]),
        "mixed_types_literal": "[True, None, 'hello', {'key': 'val'}]",                                         
    }
    checker = ItemPresenceChecker()
    logger.info("Initializing production utility check...")
    result = checker.check_presence(target_item, sources_data)
    checker.log_check_result(target_item, result)
    if not result:
        logger.error(f"Target item {target_item} was not found in any provided data source.")
if __name__ == '__main__':
    run_main()