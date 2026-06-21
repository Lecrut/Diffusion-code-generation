from dataclasses import dataclass
from typing import List, Dict
ENTRY_AGE_THRESHOLD = 20

@dataclass(frozen=True)
class StoreEntry:
    name: str
    age: int

def process_store_entries(entries: List[StoreEntry]) -> Dict[int, List[str]]:
    summary = {}
    for entry in entries:
        if entry.age not in summary:
            summary[entry.age] = []
        if entry.age > ENTRY_AGE_THRESHOLD:
            summary[entry.age].append(entry.name)
    return summary
if __name__ == '__main__':
    store_entries = [StoreEntry('Alice', 30), StoreEntry('Bob', 25), StoreEntry('Charlie', 30), StoreEntry('David', 25), StoreEntry('Eve', 18)]
    result = process_store_entries(store_entries)
    print(result)