from typing import Dict, Any
def check_name_exists(names: Dict[str, Any], target_name: str) -> bool:
    return target_name in names
if __name__ == '__main__':
    sample_data: Dict[str, int] = {"Alice": 30, "Bob": 25}
    test_cases: list[tuple[str, bool]] = [
        ("Alice", True),
        ("Charlie", False),
        ("alice", False)
    ]
    for name, expected in test_cases:
        result = check_name_exists(sample_data, name)
        assert result == expected, f"Failed for '{name}'"