from collections import Counter, defaultdict
def check_existence(target: str) -> bool:
    data_structures = [
        ["apple", "banana", "cherry"],
        {"fruit": "grape"},
        {101: "orange", 102: "pear"},
        ("mango", "kiwi"),
        Counter({"melon": 5, "lemon": 3}),
    ]
    for structure in data_structures:
        if isinstance(structure, dict):
            if target in structure.values():
                return True
        elif isinstance(structure, set) or isinstance(structure, tuple):
            if target in structure:
                return True
        else:
            try:
                if any(item == target for item in structure):
                    return True
            except TypeError:
                continue
    return False
if __name__ == '__main__':
    test_strings = ["banana", "grapefruit", "nonexistent"]
    results = []
    for s in test_strings:
        found = check_existence(s)
        results.append(f"'{s}' exists: {found}")
    print("\n".join(results))