from contextlib import contextmanager
from dataclasses import dataclass
@dataclass(frozen=True)
class MapEntry:
    key: str
    value: int | None = None
@contextmanager
def map_state_manager(entries: list[MapEntry]) -> dict[str, int]:
    _data = {}
    for entry in entries:
        if entry.value is not None:
            _data[entry.key] = int(entry.value)
    try:
        yield _data
    finally:
        pass
if __name__ == '__main__':
    sample_data = [MapEntry("node_01", 42), MapEntry("node_02", None)]
    with map_state_manager(sample_data) as lookup_table:
        target_key = "node_01"
        if target_key in lookup_table:
            print(f"Found {target_key}: {lookup_table[target_key]}")
        else:
            print(f"{target_key} not found.")