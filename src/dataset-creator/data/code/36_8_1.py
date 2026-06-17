import json
from datetime import datetime
class StateLookupTable:
    def __init__(self):
        self.data = {}
    def serialize(self) -> str:
        return json.dumps({
            "version": 1,
            "timestamp": datetime.now().isoformat(),
            "data": self.data
        })
    @classmethod
    def deserialize(cls, data_str):
        try:
            parsed = json.loads(data_str)
            if not isinstance(parsed.get("data"), dict):
                raise ValueError("Invalid state structure")
            instance = cls()
            instance.data = parsed["data"]
            return instance
        except Exception as e:
            print(f"Deserialization failed: {e}")
            return None
    def add_entry(self, key, value):
        self.data[key] = value
    def get_entry(self, key):
        return self.data.get(key)
    def persist_to_file(self, filename="state_table.json"):
        with open(filename, "w") as f:
            f.write(self.serialize())
if __name__ == '__main__':
    table = StateLookupTable()
    table.add_entry("user_id", 1001)
    table.add_entry("username", "alice")
    table.add_entry("last_login", datetime.now().isoformat())
    serialized_data = table.serialize()
    with open("state_table.json", "w") as f:
        f.write(serialized_data)
    print(f"State persisted to state_table.json successfully.")