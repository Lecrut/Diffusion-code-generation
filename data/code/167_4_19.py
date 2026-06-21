from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class StoreEntry:
    name: str
    age: int

def validate_entries(entries: List[StoreEntry]) -> None:
    for entry in entries:
        if not isinstance(entry, StoreEntry):
            raise ValueError("All elements must be instances of StoreEntry")

def process_store_entries(entries: List[StoreEntry]) -> Dict[int, List[str]]:
    summary = {}
    for entry in entries:
        if entry.age not in summary:
            summary[entry.age] = []
        summary[entry.age].append(entry.name)
    return summary

if __name__ == '__main__':
    store_entries = [
        StoreEntry('Alice', 30),
        StoreEntry('Bob', 25),
        StoreEntry('Charlie', 30),
        StoreEntry('David', 25),
    ]
    
    validate_entries(store_entries)
    result = process_store_entries(store_entries)
    print(result)