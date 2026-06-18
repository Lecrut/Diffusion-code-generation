from dataclasses import dataclass
from typing import Dict, Optional
@dataclass(frozen=True)
class MapEntry:
    key: str
    value: int
    def __post_init__(self):
        if not isinstance(self.key, str):
            raise TypeError("Key must be a string.")
@dataclass(frozen=True)
class MapState:
    entries: Dict[str, int] = None
    def __post_init__(self):
        if self.entries is None:
            self.entries = {}
def get_map_state() -> MapState:
    return MapState(entries={})
class LookupService:
    def __init__(self, state_manager=None):
        self._state = get_map_state() if state_manager is None else state_manager
    @property
    def entries(self) -> Dict[str, int]:
        return self._state.entries.copy()
    def add_entry(self, key: str, value: int) -> bool:
        try:
            self._state.entries[key] = value
            return True
        except Exception as e:
            print(f"Error adding entry: {e}")
            return False
    def get_entry(self, key: str) -> Optional[int]:
        return self._state.entries.get(key)
def main():
    initial_state = MapState(entries={"alpha": 10, "beta": 20})
    lookup_service = LookupService(state_manager=initial_state)
    print("Initial entries:", list(lookup_service.entries.keys()))
    success = lookup_service.add_entry("gamma", 30)
    if not success:
        return
    print(f"Added 'gamma' with value {30}")
    retrieved_value = lookup_service.get_entry("beta")
    assert retrieved_value == 20, "Value mismatch for beta."
    try:
        _ = lookup_service.get_entry("nonexistent_key")
    except KeyError as e:
        print(f"KeyError raised correctly: {e}")
if __name__ == '__main__':
    main()