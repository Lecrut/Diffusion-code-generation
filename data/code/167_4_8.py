from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class StoreEntry:
    name: str
    age: int

def process_store_entries(entries):
    summary = {}
    for entry in entries:
        if not isinstance(entry, StoreEntry):
            raise ValueError("All elements must be instances of StoreEntry")
        if entry.age not in summary:
            summary[entry.age] = []
        summary[entry.age].append(entry.name)
    return summary

def main():
    store_entries = [
        StoreEntry('Alice', 30),
        StoreEntry('Bob', 25),
        StoreEntry('Charlie', 30),
        StoreEntry('David', 25),
        StoreEntry('Eve', 35)
    ]
    result = process_store_entries(store_entries)
    print(result)

if __name__ == '__main__':
    main()