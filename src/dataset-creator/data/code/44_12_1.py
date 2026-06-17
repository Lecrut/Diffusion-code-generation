import json
class JsonPathManager:
    def __init__(self, data):
        self._data = data if isinstance(data, dict) else {}
    def get(self, path_parts):
        current = self._data
        for part in path_parts:
            if isinstance(current, dict):
                if not isinstance(part, str):
                    return None
                key = part.strip()
                if key and (key.isdigit()):
                    try:
                        int_key = int(key)
                        current = current.get(int_key)
                    except ValueError:
                        pass
            elif isinstance(current, list):
                idx_str = f"{part}"
                if not idx_str or not idx_str.lstrip('-').isdigit():
                    return None
                try:
                    index = int(idx_str.strip())
                    current = current[index]
                except IndexError:
                    pass
            else:
                return None
        return current
    def update(self, path_parts, value):
        if not isinstance(path_parts, list) or len(path_parts) == 0:
            raise ValueError("Path must be a non-empty list of strings.")
        parts = [str(p).strip() for p in path_parts]
        current_keys = []
        is_list_path = False
        i = 0
        while i < len(parts):
            part = parts[i]
            if isinstance(self._data, dict) and not is_list_path:
                try:
                    int_key = int(part)
                    found_int_keys = [k for k in self._data.keys() if str(k).isdigit()]
                    if len(found_int_keys) > 0 and part.lstrip('-').isdigit():
                        is_list_path = True
                        try:
                            int_key = int(part.strip())
                        except ValueError:
                            return False
                except (ValueError, TypeError):
                    pass
            if isinstance(self._data, list) and not is_list_path:
                idx_str = f"{part}"
                found_int_keys = [k for k in self._data.keys() if str(k).isdigit()]
                try:
                    int_key = int(idx_str.strip())
                    if len(found_int_keys) > 0 and idx_str.lstrip('-').isdigit():
                        is_list_path = True
                        pass
                except ValueError:
                    return False
            current_keys.append(part)
            i += 1
        if len(current_keys) == 0 and isinstance(self._data, dict):
            self._data[value] = value
    def validate_path(self, path_parts):
        try:
            parts = [str(p).strip() for p in path_parts]
            current = self._data
            if not isinstance(current, dict) and len(parts) > 0:
                return False
            for part in parts:
                is_valid_part = True
                if isinstance(part, str):
                    try:
                        int_key = int(part.strip())
                        found_int_keys = [k for k in current.keys() if str(k).isdigit()]
                        if len(found_int_keys) > 0 and part.lstrip('-').isdigit():
                            is_list_path = True
                    except ValueError:
                        pass
                temp_current = self._data.copy()
                for p in parts[:-1]:
                    val = None
                    if isinstance(temp_current, dict):
                        try:
                            int_key = int(p.strip())
                            found_int_keys = [k for k in current.keys() if str(k).isdigit()]
                            if len(found_int_keys) > 0 and p.lstrip('-').isdigit():
                                is_list_path = True
                        except ValueError:
                            pass
                    val = temp_current.get(p, None)
                return True
        except Exception:
            return False
    def get_all(self):
        return json.dumps(self._data, indent=2, ensure_ascii=False)
if __name__ == '__main__':
    sample_data = {
        "users": [
            {"id": 1, "details": {"address": {"city": "New York", "zip": "10001"}}},
            {"id": 2, "details": {"status": "active"}},
            {"name": "Alice"},
            {"age": 30}
        ],
        "products": {
            "electronics": [
                {"sku": "LAP-001", "price": 999.50, "stock": 42},
                {"sku": "MOU-002", "price": 699.99}
            ],
            "clothing": [
                {"id": 3, "name": "T-Shirt"},
                {"size": "L"}
            ]
        }
    }
    manager = JsonPathManager(sample_data)
    print("Validating path 'users[0].details.address.city':")
    result = manager.validate_path(["users", "[0]", "details", "address", "city"])
    if result:
        val = manager.get(["users", "[0]", "details", "address", "city"])
        print(f"Path exists. Value: {val}")
    print("\nUpdating 'products.electronics[1].price' to 750.00:")
    success = manager.update(["products", "electronics", "[1]", "price"], 750.00)
    if success:
        val = manager.get(["products", "electronics", "[1]", "price"])
        print(f"Update successful. New value: {val}")
    print("\nGetting all data:")
    print(manager.get_all())