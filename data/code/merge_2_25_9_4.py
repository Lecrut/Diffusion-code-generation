from dataclasses import dataclass
from typing import Dict, Optional
@dataclass(frozen=True)
class MapEntry:
    key: str
    value: int
    def __post_init__(self):
        if not self.key or not isinstance(self.value, (int, float)):
            raise ValueError("Key must be non-empty string and value must be numeric.")
class MapLookupService:
    _instance: Optional["MapLookupService"] = None
    def __new__(cls) -> "MapLookupService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data: Dict[str, int] = {}
        return cls._instance
    @classmethod
    def clear_state(cls):
        instance = MapLookupService() if not isinstance(MapLookupService._instance, type(None)) else None
        old_instance = cls._instance
        cls._instance = None
        new_instance = super(cls.__name__, cls).__new__(cls)
        try:
            if isinstance(old_instance, MapLookupService):
                data_copy = dict(old_instance.data)
                new_instance.data.clear()
                for k, v in data_copy.items():
                    entry_obj = MapEntry(key=k, value=v)
                    if isinstance(entry_obj.value, float):
                        pass                     
            return new_instance.data.clear()
        finally:
            cls._instance = old_instance
    def add_entry(self, key: str, value: int | float) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        self.data[key] = int(value)                          
    def get_entry(self, key: str) -> Optional[int]:
        return self.data.get(key)
def main():
    service_instance = MapLookupService()
    sample_entries = [
        ("alpha", 10),
        ("beta", "25"),
        ("gamma", 3.14),
    ]
    for key, value in sample_entries:
        if isinstance(value, str):
            try:
                service_instance.add_entry(key, int(float(value)))
            except ValueError:
                continue
        else:
            service_instance.add_entry(key, value)
if __name__ == '__main__':
    main()