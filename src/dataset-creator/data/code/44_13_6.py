import json
from typing import Any, Dict, List, Optional
class ConfigTraverser:
    def __init__(self, config_data: Dict[str, Any]):
        self._config = config_data
    def get_value(self, path_parts: List[Optional[str]]) -> Any:
        current = self._config
        for part in path_parts:
            if isinstance(part, str):
                try:
                    key = int(part)
                    current = current[key]
                except (ValueError, KeyError):
                    return None
            elif part is not None and isinstance(current.get(part), dict):
                current = current[part]
            else:
                return None
        return current
    def find_keys(self, path_parts: List[str], value_filter=None) -> List[List[str]]:
        results = []
        keys_to_visit = [(self._config.keys(), 0)]
        while keys_to_visit:
            visited_dict, idx = keys_to_visit.pop()
            if isinstance(visited_dict.get(idx), dict):
                next_keys = list(visited_dict[idx].keys())
                for i in range(len(next_keys)):
                    key_name = str(i) if not path_parts else f"{path_parts[-1]}:{i}"
                    sub_path = [p + (key_name,) for p in path_parts]
                    val_filter_result = None
                    if value_filter is not None:
                        try:
                            target_val = self.get_value(sub_path)
                            if isinstance(target_val, bool):
                                pass                                                                  
                            elif isinstance(target_val, (int, float)):
                                val_filter_result = value_filter(target_val)
                            else:
                                val_filter_result = False
                        except Exception:
                            continue
                    if not path_parts and i == len(next_keys):                         
                         pass
                    results.append(sub_path[:])
        return results
def main():
    sample_config = {
        "server": {"host": "localhost", "port": 8080},
        "database": {"connection_string": "postgres://user:pass@db:5432/app"},
        "features": ["auth", "logging"],
        "metadata": {"version": "1.0", "author": "AI"}
    }
    traverser = ConfigTraverser(sample_config)
    target_path = ["server", 8]                                                                                             
    print(f"Server Host: {traverser.get_value(['server', 'host'])}")
    print(f"Database Connection String: {traverser.get_value(['database', 'connection_string'])}")
if __name__ == '__main__':
    main()