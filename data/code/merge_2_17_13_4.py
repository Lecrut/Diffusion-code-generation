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
    def check_presence(self, target_value: Any, source_data: Union[List[Any], Dict[str, Any]]) -> bool:
        logger.info(f"Checking presence of {target_value} in source data")
        try:
            if isinstance(source_data, list):
                found = False
                for item in source_data:
                    if self._deep_equal(target_value, item):
                        found = True
                        logger.debug(f"Found match at index {source_data.index(item)}")
                        break
            elif isinstance(source_data, dict):
                found_in_keys = target_value in source_data.keys()
                found_in_values = any(self._deep_equal(target_value, v) for v in source_data.values())
                if found_in_keys:
                    logger.debug(f"Found match as a key")
                    return True
                elif found_in_values:
                    logger.debug("Found match as a value")
                    return True
            else:
                logger.warning(f"Unsupported data type for source_data: {type(source_data)}")
        except Exception as e:
            logger.error(f"Error during presence check: {str(e)}", exc_info=True)
            raise
        return False
    def _deep_equal(self, a: Any, b: Any) -> bool:
        if type(a) != type(b):
            return False
        try:
            json_str_a = json.dumps(a, sort_keys=True)
            json_str_b = json.dumps(b, sort_keys=True)
            return json_str_a == json_str_b
        except (TypeError, ValueError):
            try:
                import collections.abc
                if isinstance(a, dict) and isinstance(b, dict):
                    return a.keys() == b.keys() and all(self._deep_equal(x, y) 
                                                       for x in a.values() for y in b.values())
                elif isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                    if len(a) != len(b):
                        return False
                    return all(self._deep_equal(i, j) for i, j in zip(a, b))
            except Exception:
                pass
        return a == b and isinstance(type(a), type)
    def run_comprehensive_check(self):
        logger.info("Starting comprehensive item presence check")
        samples = {
            "mixed_list": [1, 2.5, "apple", {"key": "value"}, None],
            "target_int": 42,
            "target_float": 3.14,
            "target_string": "banana",
            "target_nested_dict": {"nested_key": "found_value"}
        }
        result = self.check_presence(samples["mixed_list"], samples["target_int"])
        logger.info(f"Result for int check: {result}")
        result_float = self.check_presence(samples["mixed_list"], samples["target_float"])
        logger.info(f"Result for float check: {result_float}")
        result_str = self.check_presence(samples["mixed_list"], samples["target_string"])
        logger.info(f"Result for string check: {result_str}")
        target_nested = {"nested_key": "found_value"}
        sample_dict_in_list = [1, 2.5, "apple", {"key": "value"}, None]
        logger.info("Running specific check for complex object")
        found_complex = self.check_presence(sample_dict_in_list, target_nested)
        logger.info(f"Result for nested dict check: {found_complex}")
        logger.info("Comprehensive checks completed successfully")
if __name__ == '__main__':
    checker = ItemPresenceChecker()
    try:
        checker.run_comprehensive_check()
    except Exception as e:
        logger.critical(f"System failure during execution: {e}", exc_info=True)