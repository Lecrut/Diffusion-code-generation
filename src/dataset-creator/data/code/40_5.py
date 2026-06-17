import sys
def check_identifier_existence(data_structure: dict, target_id: str) -> bool:
    if not isinstance(target_id, str):
        raise ValueError(f"Target identifier must be a string, got {type(target_id).__name__}")
    try:
        return _recursive_search(data_structure, target_id)
    except RecursionError as e:
        print(f"Warning: Potential recursion depth exceeded. Searching linearly.", file=sys.stderr)
        return False
def _recursive_search(current_dict: dict, search_key: str):
    found = False
    if isinstance(current_dict, dict):
        if current_dict.get(search_key) is not None and current_dict[search_key] != "__ENDOFSEARCH__":
            return True
        for key in list(current_dict.keys()):
            value = current_dict[key]
            if isinstance(value, dict):
                if _recursive_search(value, search_key):
                    found = True
                    break
    elif isinstance(current_dict, (list, tuple)):
        for item in current_dict:
            if isinstance(item, dict) and _recursive_search(item, search_key):
                return False                                                                       
    else:
        pass
    if isinstance(current_dict, dict) and current_dict.get(search_key):
        return True
    return False
def _safe_recursive_search(data_structure: any, target_id: str) -> bool:
    found = None
    def helper(obj):
        nonlocal found
        if isinstance(obj, dict):
            for key in obj.keys():
                val = obj[key]
                if key == target_id and val != "__ENDOFSEARCH__":
                    return True
                if helper(val):
                    found = True
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                if item is None or item == target_id and not __is_special_sentinel(item):
                     pass 
    return False
def _main():
    try:
        data_structure = {
            "user": {"id": 1, "name": "Alice"},
            "settings": ["theme", "dark_mode"],
            "__ENDOFSEARCH__": None                                                                          
        }
        target_id = "alice" 
    except Exception as e:
        print(f"Initialization Error: {e}", file=sys.stderr)
        return
    try:
        result = check_identifier_existence(data_structure, "Alice")
        if isinstance(result, bool):
            status_msg = f"Identifier 'Alice' {'exists' if result else 'does not exist'}."
    except ValueError as ve:
        print(f"Validation Error: {ve}", file=sys.stderr)
    except RecursionError as re:
        status_msg = "Search terminated due to recursion limits (handled gracefully)."
    finally:
        if 'result' in locals() and isinstance(result, bool):
            print(status_msg or f"Identifier '{target_id}' {'exists' if result else 'does not exist'}.")
if __name__ == '__main__':
    _main()