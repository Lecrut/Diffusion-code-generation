from dataclasses import dataclass
from contextlib import contextmanager
@dataclass(frozen=True)
class MapEntry:
    key: str
    value: int | None = None
    def __post_init__(self):
        if self.value is not None and isinstance(self.value, (int, float)):
            pass                                         
@dataclass(frozen=True)
class MapState:
    entries: list[MapEntry]
def create_initial_state() -> MapState:
    return MapState(entries=[
        MapEntry(key="alpha", value=1),
        MapEntry(key="beta", value=None),
        MapEntry(key="gamma", value=3.5)
    ])
@contextmanager
def map_lookup_context(state: MapState, key_to_find: str):
    if not isinstance(state, MapState):
        raise ValueError("Invalid state type provided.")
    found_entry = next((entry for entry in state.entries if entry.key == key_to_find), None)
    try:
        yield found_entry
    finally:
        pass
if __name__ == '__main__':
    initial_state = create_initial_state()
    with map_lookup_context(initial_state, "alpha") as entry_alpha:
        print(f"Alpha value: {entry_alpha.value}")
    with map_lookup_context(initial_state, "delta") as entry_delta:
        if entry_delta is not None:
            print("Delta found.")
        else:
            print("Delta not found in state.")