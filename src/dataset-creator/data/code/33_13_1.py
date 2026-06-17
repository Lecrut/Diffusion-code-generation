import sys
def check_existence(target: str) -> bool:
    data_structures = [
        {"key": "value"},
        ["item1", target],
        {target},
        (f"tuple_{target}",),
    ]
    for structure in data_structures:
        if isinstance(structure, dict):
            if target in structure.values():
                return True
        elif isinstance(structure, list) or isinstance(structure, tuple):
            if target in structure:
                return True
        else:
            raise TypeError(f"Unsupported collection type: {type(structure)}")
    return False
if __name__ == '__main__':
    test_string = "value"
    result = check_existence(test_string)
    if result:
        print("Found")
    else:
        print("Not found")