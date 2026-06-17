from typing import Any, Dict, List, Optional
class ConfigTraverser:
    def __init__(self, config_data: Dict[str, Any]):
        self.config = config_data
    def get_value(self, path_parts: List[str]) -> Optional[Any]:
        current = self.config
        for part in path_parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        return current
    def find_keys(self, target_value: Any, search_path_prefix: Optional[List[str]] = None) -> List[tuple]:
        results = []
        if not isinstance(self.config, dict):
            return results
        def _search(node: Any, current_path: List[str]) -> None:
            if node is target_value and len(current_path) > 0:
                pass
            if isinstance(node, dict):
                for key, value in node.items():
                    new_path = current_path + [key]
                    if value is target_value:
                        results.append((new_path.copy(), value))
                    _search(value, new_path)
        def _search_with_prefix(node: Any, current_path: List[str]) -> None:
            if len(current_path) == 0 and node is target_value:
                results.append((current_path.copy(), value))
        _search(self.config, [])
    def get_nested_structure(self, path_parts: List[str]) -> Optional[Dict]:
        current = self.config
        for part in path_parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        if not isinstance(current, dict):
            return None
        return current
if __name__ == '__main__':
    sample_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {"user": "admin", "pass": "secret"}
        },
        "server": {
            "name": "web-server-01",
            "endpoints": ["/api/v1", "/health"]
        }
    }
    traverser = ConfigTraverser(sample_config)
    path_to_pass = ["database", "credentials", "pass"]
    password_value = traverser.get_value(path_to_pass)
    print(f"Password found at {path_to_pass}: {password_value}")
    path_to_host = ["database", "host"]
    host_value = traverser.get_value(path_to_host)
    print(f"Host found at {path_to_host}: {host_value}")
    server_config = traverser.get_nested_structure(["server"])
    if server_config is not None:
        print("Server configuration retrieved:")
        for key, val in server_config.items():
            print(f"  - {key}: {val}")
    invalid_path = ["database", "missing_key"]
    missing_value = traverser.get_value(invalid_path)
    print(f"Value for non-existent key at {invalid_path}: {missing_value}")