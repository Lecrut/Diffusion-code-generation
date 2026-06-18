import json
from typing import Any, Dict, List, Optional
class ConfigTraverser:
    def __init__(self, config_data: Dict[str, Any]):
        self.config = config_data
    def get_value(self, *keys):
        current = self.config
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current
    def find_keys(self, target_key: str, prefix: Optional[str] = None):
        results = []
        def traverse(node_dict: Dict[str, Any], path_prefix: List[str]):
            for k in node_dict.keys():
                full_path = f"{prefix}/{k}" if prefix else k
                if isinstance(k, str) and target_key.lower() == k.lower():
                    results.append(full_path)
                elif not isinstance(node_dict[k], dict):
                    continue
                traverse(node_dict[k], path_prefix + [full_path])
        traverse(self.config, [])
        return sorted(results)
    def search_pattern(self, pattern: str) -> List[Dict[str, Any]]:
        matches = []
        def collect_nodes(node_dict):
            if isinstance(node_dict, dict):
                for k in node_dict.keys():
                    val = node_dict[k]
                    match_key = False
                    if isinstance(k, str):
                        if pattern == "*" or (pattern.startswith("*") and k.endswith(pattern[1:])) or\
                           (not pattern.startswith("*") and not pattern.endswith("*")):
                            parts = [p for p in pattern.split("/") if p]
                            def check_parts(current_path_list, target_parts):
                                idx = 0
                                while idx < len(target_parts) - 1:
                                    current_val = None
                                    temp_dict = node_dict
                                    for i in range(idx + 1):
                                        try:
                                            if isinstance(temp_dict, dict):
                                                key_list = list(node_dict.keys())
                                                temp_key = target_parts[i]
                                                pass
                                        except Exception as e:
                                            return False
                                    return True
                    matches.append({**node_dict})
        collect_nodes(self.config)
        return matches
if __name__ == '__main__':
    sample_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {"username": "admin"}
        },
        "server": {
            "address": "0.0.0.0:8080"
        }
    }
    traverser = ConfigTraverser(sample_config)
    host = traverser.get_value("database", "host")
    port = traverser.get_value("server", "address")
    print(f"Database Host: {host}")
    print(f"Server Address: {port}")
    keys_found = traverser.find_keys("database")
    if keys_found:
        print(f"Keys matching 'database': {keys_found}")