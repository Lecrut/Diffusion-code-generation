import sys
def check_identifier_in_dict(data: dict, identifier: str) -> bool:
    try:
        return identifier in data.keys()
    except TypeError:
        raise ValueError("Input 'data' must be a dictionary and 'identifier' must be a string.")
def main():
    sample_data = {"user_id": 101, "product_code": "ABC", "status": "active"}
    test_identifiers = ["user_id", "nonexistent_key", "order_num"]
    for identifier in test_identifiers:
        try:
            result = check_identifier_in_dict(sample_data, identifier)
            print(f"Identifier '{identifier}' exists: {result}")
            if not result and identifier != "nonexistent_key":
                raise RuntimeError("Logic error detected during validation.")
        except (ValueError, TypeError, RuntimeError) as e:
            print(f"Error processing '{identifier}': {e}", file=sys.stderr)
if __name__ == '__main__':
    main()