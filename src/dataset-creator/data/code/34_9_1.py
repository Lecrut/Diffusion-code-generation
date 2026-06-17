import json
import sqlite3
from typing import Any, Dict, List, Optional
class DataLoader:
    def __init__(self):
        self.storage_backends = {}
    def register_backend(self, name: str, backend_class) -> None:
        if not isinstance(backend_class, type) or issubclass(backend_class, StorageBackendBase):
            raise ValueError("Invalid backend class provided.")
        self.storage_backends[name] = backend_class
    def load_data(self, source_config: Dict[str, Any]) -> List[Any]:
        if "source_type" not in source_config or "data_items" not in source_config:
            raise ValueError("Invalid source configuration. Missing 'source_type' and 'data_items'.")
        items = []
        item_id_counter = 0
        if source_config["source_type"] == "json":
            for i, data in enumerate(source_config.get("data_items", [])):
                item_id_counter += 1
                item = {
                    "id": item_id_counter,
                    "type": "JSON_ITEM",
                    **data
                }
                items.append(item)
        elif source_config["source_type"] == "csv_simulated":
            for i in range(3):
                item_id_counter += 1
                item = {
                    "id": item_id_counter,
                    "type": "CSV_ITEM",
                    "value": f"Sample value {i}",
                    "category": source_config.get("data_items", [{}])[0].get("category", "default") if source_config.get("data_items") else None
                }
                items.append(item)
        return items
class StorageBackendBase:
    def save(self, data_list: List[Any]) -> int:
        raise NotImplementedError
    def get_count(self) -> int:
        raise NotImplementedError
class JsonStorage(StorageBackendBase):
    def __init__(self, file_path: str = "data.json"):
        self.file_path = file_path
        self.data_file_exists = False
    def save(self, data_list: List[Any]) -> int:
        with open(self.file_path, 'w') as f:
            json.dump(data_list, f)
        return len(data_list)
    def get_count(self) -> int:
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return len(data) if isinstance(data, list) else 0
        except FileNotFoundError:
            return 0
class SqliteStorage(StorageBackendBase):
    def __init__(self, db_file: str = "data.db"):
        self.db_path = db_file
    def save(self, data_list: List[Any]) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, value TEXT)")
        inserted_count = 0
        for item in data_list:
            try:
                if isinstance(item.get('value'), str):
                    cursor.execute(
                        "INSERT INTO items (type, value) VALUES (?, ?)",
                        (item['type'], item['value'])
                    )
                    inserted_count += 1
            except KeyError as e:
                print(f"Skipping item due to missing key {e}")
        conn.commit()
        cursor.close()
        conn.close()
        return inserted_count
    def get_count(self) -> int:
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM items")
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except Exception as e:
            print(f"Error retrieving count from database: {e}")
            return 0
class MainApp:
    def __init__(self):
        self.loader = DataLoader()
    def run(self) -> None:
        json_backend_path = "output/data.json"
        sqlite_backend_path = "output/data.db"
        try:
            import os
            if not os.path.exists("output"):
                os.makedirs("output")
            self.loader.register_backend("json_storage", JsonStorage)
            self.loader.register_backend("sqlite_storage", SqliteStorage)
            json_config = {
                "source_type": "json",
                "data_items": [
                    {"name": "Alice", "age": 30},
                    {"name": "Bob", "age": 25}
                ]
            }
            sqlite_config = {
                "source_type": "csv_simulated"
            }
            json_items = self.loader.load_data(json_config)
            if not os.path.exists("output"):
                os.makedirs("output")
            json_storage = JsonStorage(json_backend_path)
            count_json = json_storage.save(json_items)
            print(f"Saved {count_json} items to JSON storage.")
            sqlite_items = self.loader.load_data(sqlite_config)
            if not os.path.exists("output"):
                os.makedirs("output")
            sqlite_storage = SqliteStorage(sqlite_backend_path)
            count_sqlite = sqlite_storage.save(sqlite_items)
            print(f"Saved {count_sqlite} items to SQLite storage.")
        except Exception as e:
            print(f"Error occurred during execution: {e}")
if __name__ == '__main__':
    app = MainApp()
    app.run()