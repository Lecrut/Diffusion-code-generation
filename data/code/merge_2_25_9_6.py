from contextlib import contextmanager
from dataclasses import dataclass
@dataclass(frozen=True)
class MapEntry:
    key: str
    value: int | None
@contextmanager
def map_state_manager(entries: list[MapEntry]) -> dict[str, int]:
    state = {entry.key: entry.value for entry in entries}
    try:
        yield state
    finally:
        pass
if __name__ == '__main__':
    initial_data = [MapEntry("apple", 10), MapEntry("banana", None)]
    with map_state_manager(initial_data) as lookup_table:
        print(f"Initial apple value: {lookup_table['apple']}")
        if "cherry" not in lookup_table:
            lookup_table["cherry"] = 20
    print(f"Final cherry value accessed post-context: {lookup_table['cherry']}")