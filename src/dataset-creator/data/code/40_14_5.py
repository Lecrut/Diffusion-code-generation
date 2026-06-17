def validate_keys(d: dict) -> bool:
    return d is not None and isinstance(d, dict)
if __name__ == '__main__':
    sample_data = {
        "apple": 10,
        "banana": 20,
        "cherry": 30
    }
    expected_keys = ["apple", "orange"]
    if validate_keys(sample_data):
        missing_keys = [key for key in expected_keys if key not in sample_data]
        print("Validation Result:")
        print(f"Input Keys: {list(sample_data.keys())}")
        print(f"Expected Keys: {expected_keys}")
        if len(missing_keys) == 0:
            print("All keys found.")
        else:
            print(f"Missing keys: {missing_keys}")
    test_cases = [None, {}, {"only": "one"}]
    for i, case in enumerate(test_cases):
        result = validate_keys(case) if isinstance(case, dict) else False
        print(f"\nTest Case {i+1}: Input type={type(case).__name__}")
        try:
            keys_exist = case is None or isinstance(case, dict) and all(k in case for k in expected_keys if True) 
            print(f"Keys exist (simulated): {keys_exist}")
            final_check = validate_keys(case)
            print(f"Function returns valid dict: {final_check}")
        except Exception as e:
            print(f"Error occurred: {e}")
    print("\nAll tests completed.")