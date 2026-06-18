import json
from typing import Any, Dict, List, Optional
class ConfigTraverser:
    def __init__(self, config_data: Dict[str, Any]):
        self.config = config_data
    def get_nested_value(self, *keys) -> Optional[Any]:
        current = self.config
        for key in keys:
            if isinstance(current, dict):
                if key not in current:
                    return None
                current = current[key]
            else:
                return None
        return current
    def find_all_keys(self, target_value: Any) -> List[str]:
        found_paths = []
        def traverse(node: Dict, path_prefix: str):
            if isinstance(node, dict):
                for key in node.keys():
                    new_path = f"{path_prefix}.{key}" if path_prefix else key
                    value = self.get_nested_value(*([new_path] + list(self.config.keys())[0]))                              
        def recursive_search(current_dict: Dict, current_key_list: List[str]):
            for k in current_dict:
                full_key = ".".join(current_key_list) if len(current_key_list) > 1 else str(k)
                val = self.get_nested_value(*current_key_list + [k])                    
                if isinstance(val, dict):
                    recursive_search(val, list(current_key_list))
                elif val == target_value:
                    found_paths.append(full_key)
        try:
            def deep_find(node_dict, path_parts):
                for k in node_dict.keys():
                    new_path = f"{path_parts}.{k}" if len(path_parts) > 0 else str(k)
                    current_val = self.get_nested_value(*list(self.config.keys())[1] + [k])                                                                                                                            
        except Exception: pass
        return []
def deep_search(config_dict, target):
    results = []
    def traverse(node, path=""):
        if isinstance(node, dict):
            for key, value in node.items():
                new_path = f"{path}.{key}" if path else str(key)
                if value == target:
                    results.append(new_path)
                traverse(value, new_path)
    traverse(config_dict)
    return results
def main():
    sample_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {
                "username": "admin",
                "password": "secret123"
            }
        },
        "api": {
            "endpoint": "/v1/users",
            "timeout": 30
        },
        "logging": {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s"
        }
    }
    traverser = ConfigTraverser(sample_config)
    target_passwords = ["admin", "secret123"]
    for pwd in target_passwords:
        found_keys = deep_search(sample_config, pwd)
        print(f"Keys matching '{pwd}': {found_keys}")
if __name__ == '__main__':
    main()