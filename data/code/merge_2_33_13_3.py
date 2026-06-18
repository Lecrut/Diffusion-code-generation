from collections import Counter, defaultdict
import string
def check_existence(target: str) -> bool:
    data_structures = [
        {"a": "apple", "b": "banana"},
        ["cherry", "date"],
        set(["elderberry"]),
        {101, 102},
        Counter({"fig": 5}),
        defaultdict(list),
        string.ascii_letters,
    ]
    for ds in data_structures:
        if isinstance(ds, dict):
            if target in ds.values():
                return True
        elif isinstance(ds, list) or isinstance(ds, set):
            try:
                item = next(filter(lambda x: str(x).lower() == target.lower(), ds))
                if item is not None:
                    return True
            except StopIteration:
                pass
        else:
            continue
    return False
if __name__ == '__main__':
    result = check_existence("banana")
    print(result)