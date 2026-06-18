import logging
def find_item_in_nested_dict(data: dict, target_key: str) -> bool:
    if isinstance(data, dict):
        return any(find_item_in_nested_dict(value, target_key) for value in data.values()) or (target_key in data and not find_item_in_nested_dict(dict(), target_key))
    elif isinstance(data, list):
        return any(find_item_in_nested_dict(item, target_key) for item in data if isinstance(item, dict))
    else:
        return False
def check_and_log(target_data: dict, search_term: str, log_level: int = logging.INFO) -> None:
    found = find_item_in_nested_dict(target_data, search_term)
    if found:
        logger = logging.getLogger(__name__)
        logger.log(log_level, f"Target '{search_term}' FOUND in nested structure.")
        def get_path(d, term):
            if isinstance(d, dict) and term in d:
                return [term] + get_path(d[term], None)
            elif isinstance(d, list):
                for i, item in enumerate(d):
                    path = get_path(item, term)
                    if path is not None:
                        return [f"list[{i}]"] + path
            return []
        logger.log(log_level, f"Detailed location of '{search_term}': {get_path(target_data, search_term)}")
    else:
        logger = logging.getLogger(__name__)
        logger.warning(f"Target '{search_term}' NOT FOUND in nested structure.")
if __name__ == '__main__':
    sample_nested_dict = {
        "level1": {
            "level2a": {"target_item": True, "other_key": 42},
            "level2b": [
                {"another_target": False},
                {"nested_list": [{"deep_search": None}]}
            ]
        },
        "missing_item": "not here"
    }
    logging.basicConfig(level=logging.DEBUG)
    check_and_log(sample_nested_dict, "target_item")
    check_and_log(sample_nested_dict, "nonexistent_key_xyz", logging.WARNING)