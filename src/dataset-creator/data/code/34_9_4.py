import json
from typing import Any, Dict, List, Optional
class DataStorageBackend:
    def __init__(self, storage_type: str):
        self.storage_type = storage_type
    def load(self) -> List[Dict[str, Any]]:
        raise NotImplementedError()
    def persist(self, data: Dict[str, Any]) -> None:
        raise NotImplementedError()
class FileBackend(DataStorageBackend):
    def __init__(self, file_path: str = "data.json"):
        super().__init__("file")
        self.file_path = file_path
    def load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.file_path, 'r') as f:
                data_list = json.load(f)
            return data_list if isinstance(data_list, list) else []
        except FileNotFoundError:
            return []
    def persist(self, data: Dict[str, Any]) -> None:
        existing_data = self.load()
        existing_data.append(data)
        with open(self.file_path, 'w') as f:
            json.dump(existing_data, f, indent=2)
class DatabaseBackend(DataStorageBackend):
    def __init__(self, db_name: str = "main_db"):
        super().__init__("database")
        self.db_name = db_name
    def load(self) -> List[Dict[str, Any]]:
        return [
            {"id": 101, "name": "Sample Record A", "value": 3.14},
            {"id": 102, "name": "Sample Record B", "value": 2.71}
        ]
    def persist(self, data: Dict[str, Any]) -> None:
        print(f"Inserted record into {self.db_name}: {data}")
class CacheBackend(DataStorageBackend):
    def __init__(self, cache_key: str = "default_cache"):
        super().__init__("cache")
        self.cache_key = cache_key
    def load(self) -> List[Dict[str, Any]]:
        return [
            {"id": 201, "name": "Cached Item X", "value": 99},
            {"id": 202, "name": "Expired Cache Y", "value": -1}
        ]
    def persist(self, data: Dict[str, Any]) -> None:
        print(f"Updated {self.cache_key} with: {data}")
class DataLoaderManager:
    backends: List[DataStorageBackend] = []
    @classmethod
    def register_backend(cls, backend: DataStorageBackend):
        cls.backends.append(backend)
    @classmethod
    def load_all_data(self) -> Dict[str, Any]:
        all_entries = {}
        for backend in self.backends:
            entries = backend.load()
            if not isinstance(entries, list):
                continue
            entry_id_counter = 0
            for item in entries:
                unique_key = f"{backend.storage_type}_{item.get('id', 'unknown')}"
                all_entries[unique_key] = {
                    "source": backend.storage_type,
                    "data": item.copy(),
                    "entry_count": entry_id_counter + 1
                }
            entry_id_counter += 1
        return all_entries
    @classmethod
    def persist_all_data(cls) -> None:
        entries = cls.load_all_data()
        for key, value in entries.items():
            backend_name = value["source"]
            if backend_name == "file":
                file_backend = next((b for b in cls.backends if b.storage_type == "file"), None)
                if file_backend:
                    file_backend.persist(value["data"])
            elif backend_name == "database" or backend_name == "cache":
                db_or_cache_backend = next(
                    (b for b in cls.backends 
                     if b.storage_type in ["database", "cache"]), None)
                if db_or_cache_backend:
                    data_to_store = value["data"]
                    if backend_name == "database":
                        print(f"Persisting {backend_name} record for key '{key}'")
                    elif backend_name == "cache":
                        db_or_cache_backend.persist(data_to_store)
if __name__ == '__main__':
    file_storage = FileBackend(file_path="sample_data.json")
    database_storage = DatabaseBackend(db_name="production_db")
    cache_storage = CacheBackend(cache_key="session_cache")
    DataLoaderManager.register_backend(file_storage)
    DataLoaderManager.register_backend(database_storage)
    DataLoaderManager.register_backend(cache_storage)
    loaded_data = DataLoaderManager.load_all_data()
    print("Loaded entries:")
    for key, entry in loaded_data.items():
        print(f"  {key}: {entry}")
    print("\nPersisting data...")
    DataLoaderManager.persist_all_data()
    print("\nProcess completed successfully.")