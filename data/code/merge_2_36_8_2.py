import json
from datetime import datetime
class LookupTable:
    def __init__(self):
        self.data = {}
    def add_entry(self, key, value):
        if isinstance(value, (dict, list)):
            serialized_value = json.dumps(value)
        else:
            serialized_value = str(value)
        self.data[key] = {
            "value": serialized_value,
            "timestamp": datetime.now().isoformat(),
            "status": "active"
        }
    def get_entry(self, key):
        return self.data.get(key)
    def remove_entry(self, key):
        if key in self.data:
            del self.data[key]
            return True
        return False
    def serialize_to_file(self, filename="lookup_table_state.json"):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({k: v["value"] + " (meta: " + str(v.get("timestamp", "")) + ")" 
                         if isinstance(v["value"], (dict, list)) else v["value"] for k, v in self.data.items()}, f)
            return True
        except Exception as e:
            print(f"Serialization failed: {e}")
            return False
    def deserialize_from_file(self, filename="lookup_table_state.json"):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = json.load(f)
            for key in self.data.keys():
                if isinstance(content[key], dict):
                    val_data = content[key]
                    value_str = val_data.get("value", "")
                    try:
                        deserialized_value = json.loads(value_str)
                    except (json.JSONDecodeError, TypeError):
                        deserialized_value = value_str
                    self.data[key]["value"] = deserialized_value
                else:
                    if isinstance(content[key], dict):
                        val_data = content[key]
                        try:
                            deserialized_value = json.loads(val_data.get("value", ""))
                        except (json.JSONDecodeError, TypeError):
                            deserialized_value = val_data.get("value")
                        self.data[key]["value"] = deserialized_value
            return True
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return False
if __name__ == '__main__':
    table = LookupTable()
    sample_data = [
        ("user_001", {"id": 1, "role": "admin"}, True),
        ("product_a", ["item_x", "item_y"], None),
        ("config_db", {"host": "localhost", "port": 5432}, False)
    ]
    for key, value, flag in sample_data:
        table.add_entry(key, (value, flag))
    if not table.serialize_to_file():
        exit()
    print("State persisted successfully.")