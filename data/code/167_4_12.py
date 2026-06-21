from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class StoreEntry:
    name: str
    age: int

def populate_store_entries() -> List[StoreEntry]:
    return [
        StoreEntry('Alice', 30),
        StoreEntry('Bob', 25),
        StoreEntry('Charlie', 30),
        StoreEntry('David', 25)
    ]

def process_store_entries(entries: List[StoreEntry]) -> Dict[int, List[str]]:
    summary = {}
    for entry in entries:
        if entry.age not in summary:
            summary[entry.age] = []
        summary[entry.age].append(entry.name)
    return summary

if __name__ == '__main__':
    store_entries = populate_store_entries()
    result = process_store_entries(store_entries)
    print(result)