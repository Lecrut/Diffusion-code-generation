from collections import defaultdict
def check_existence(target: str) -> bool:
    data_structures = [
        ["apple", "banana", "cherry"],
        {"fruit": "grape"},
        {10, 20, 30},
        [(True,), ("hello")],
    ]
    for structure in data_structures:
        if target in structure or any(target == item for item in structure):
            return True
    return False
if __name__ == '__main__':
    test_strings = ["apple", "grapefruit", "nonexistent"]
    results = []
    for s in test_strings:
        is_found = check_existence(s)
        results.append(f"'{s}' found: {is_found}")
    print("\n".join(results))