from dataclasses import dataclass
from collections import defaultdict

@dataclass(frozen=True)
class StoreEntry:
    name: str
    age: int

def process_store_entries(entries):
    summary = defaultdict(list)
    for entry in entries:
        summary[entry.age].append(entry.name)
    return dict(summary)

if __name__ == '__main__':
    store_entries = [
        StoreEntry('Alice', 30),
        StoreEntry('Bob', 25),
        StoreEntry('Charlie', 30),
        StoreEntry('David', 25),
    ]
    result = process_store_entries(store_entries)
    print(result)