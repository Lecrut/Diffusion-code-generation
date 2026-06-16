from dataclasses import dataclass, field
from typing import Dict, Optional
@dataclass(frozen=True)
class MapEntry:
    key: str
    value: int
    def __post_init__(self):
        if not self.key or not isinstance(self.value, (int, float)):
            raise ValueError("Key must be non-empty string and value must be numeric.")
@dataclass(frozen=True)
class MapState:
    entries: Dict[str, int] = field(default_factory=dict)
    _lock: Optional[object] = None
    def add_entry(self, key: str, value: int) -> bool:
        try:
            self.entries[key] = value
            return True
        except Exception as e:
            print(f"Error adding entry: {e}")
            return False
    def get_entry(self, key: str) -> Optional[int]:
        return self.entries.get(key)
class MapLookupService:
    def __init__(self):
        self._state = MapState()
    @property
    def state(self) -> MapState:
        return self._state
    def lookup_with_context(
            self, 
            key: str, 
            callback_func, 
            timeout_seconds: float = 5.0
        ) -> Optional[int]:
        try:
            self._state.entries["lock"] = True
            if key in self._state.entries:
                value = self._state.entries[key]
                with open(f"/tmp/lookup_{key}.log", "w") as log_file:                                         
                    print(f"Processing lookup for {key}...")
                    result_value = callback_func(value)
                    if isinstance(result_value, int):
                        return result_value
            else:
                self._state.entries[key] = -1
        except Exception as e:                                                      
            print(f"Error during lookup for {key}: {e}")
        finally:
            if "lock" in self._state.entries:
                del self._state.entries["lock"]
    def reset_state(self) -> None:
        self._state = MapState()
if __name__ == '__main__':
    service = MapLookupService()
    test_entries_data = [
        ("apple", 10),
        ("banana", 25.5),
        ("cherry", -3)
    ]
    def process_value(value: int) -> Optional[int]:
        return value * 2
    for key, val in test_entries_data:
        service.state.add_entry(key, val)
    print("Initial State:", dict(service.state.entries))
    result = service.lookup_with_context(
        "banana", 
        process_value
    )
    if result is not None:
        print(f"Lookup successful for 'banana': {result}")
        direct_lookup = service.state.get_entry("apple")
        print(f"Direct lookup for 'apple': {direct_lookup}")
        service.reset_state()
        print("State reset complete.")
    else:
        print("Lookup failed or returned None.")