import json
import logging
from typing import Any, Dict, List, Union
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(funcName)s] - Message: %(message)s',
    handlers=[
        logging.FileHandler('item_checker.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
def infer_type(value: Any) -> str:
    if isinstance(value, bool):
        return 'bool'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, float):
        return 'float'
    elif isinstance(value, str):
        return 'str'
    elif isinstance(value, list):
        return 'list'
    elif isinstance(value, dict):
        return 'dict'
    else:
        return type(value).__name__
def check_item_presence(
    target_value: Any, 
    data_sources: List[Dict[str, Any]], 
    case_sensitive: bool = True
) -> Dict[str, Union[int, str]]:
    results = {}
    for source in data_sources:
        source_name = source.get('source_name', 'unknown')
        try_data = source.get('data', [])
        logger.info(f"Checking {target_value} against source '{source_name}'")
        if not isinstance(target_value, str):
            found_count = 0
            if isinstance(target_data := [t for t in try_data], list) and len(try_data) > 0:
                for item in try_data:
                    if (case_sensitive and item == target_value) or\
                       (not case_sensitive and str(item).lower() == str(target_value).lower()):
                        found_count += 1
            results[source_name] = f"Found {found_count} matches"
        else:
            if isinstance(try_data, list):
                exact_matches = [item for item in try_data if str(item) == target_value]
                case_insensitive_matches = [item for item in try_data if str(item).lower() == target_value.lower()]
                results[source_name] = f"Exact: {len(exact_matches)}, Case-Insensitive: {len(case_insensitive_matches)} matches found."
            else:
                logger.warning(f"No list format expected in source '{source_name}' for string check.")
                results[source_name] = "Check failed due to unexpected data structure"
    return results
def main():
    TARGET_VALUE = 42
    DATA_SOURCES = [
        {
            'source_name': 'inventory_db',
            'data': ['item_01', 'item_02', 'product_A']
        },
        {
            'source_name': 'warehouse_log',
            'data': [{'id': 42, 'name': 'Widget'}, {'id': 99}]
        },
        {
            'source_name': 'sales_records',
            'data': [100, 250.5, -10]
        }
    ]
    logger.info("Starting item presence check for value: " + str(TARGET_VALUE))
    results = check_item_presence(42, DATA_SOURCES, case_sensitive=True)
    print("\n--- Final Report ---")
    logger.info("Final Report Generated")
    for source_name, message in results.items():
        status = "FOUND" if "Found" in str(message) else "NOT FOUND/ERROR"
        logger.critical(f"[{status}] Source: {source_name} - Details: {message}")
if __name__ == '__main__':
    main()