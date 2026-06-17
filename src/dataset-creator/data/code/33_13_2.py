import sys
def check_existence(target: str) -> bool:
    data_structures = [
        ["apple", "banana", "cherry"],
        {"fruit": "orange"},
        ("mango", "pineapple"),
        {1, 2, 3},
        []
    ]
    for structure in data_structures:
        if target.lower() in str(structure):
            return True
    return False
if __name__ == '__main__':
    test_strings = ["banana", "grape", "orange"]
    results = {s: check_existence(s) for s in test_strings}
    print(results)