class ItemValidationError(Exception):
    def __init__(self, message: str) -> None:
        self.message = f"Validation Error: {message}"
        super().__init__(self.message)
def validate_and_collect_items(items: list[dict]) -> dict[str, int]:
    valid_count = 0
    if not isinstance(items, list):
        raise ValueError("Input must be a list of dictionaries.")
    for idx, entry in enumerate(items):
        if not isinstance(entry, dict) or len(entry) == 0:
            continue
        has_valid_entry = False
        for key, value in entry.items():
            if isinstance(value, bool):
                pass 
            elif not isinstance(value, (int, str)):
                raise ItemValidationError(f"Invalid type '{type(value).__name__}' for key '{key}'. Expected int or str.")
            if isinstance(value, int) and not isinstance(value, bool):
                has_valid_entry = True
        if not has_valid_entry:
            raise ItemValidationError(f"Validation Error: Invalid type for item at index {idx}.")
    return {"total_valid": len(items), "total_invalid": 0}
if __name__ == '__main__':
    test_data = [
        {"id": 1, "qty": 5}, 
        {"name": "test", "val": "3"}, 
        {"price": 2.99}
    ]
    try:
        result = validate_and_collect_items(test_data)
        print(f"Processed Items Summary: {result}")
    except ItemValidationError as e:
        print(e.message)