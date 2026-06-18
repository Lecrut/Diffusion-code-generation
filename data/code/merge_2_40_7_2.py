import timeit
def validate_keys_against_dict(data: dict, keys_to_check: list) -> bool:
    return all(key in data for key in keys_to_check)
if __name__ == '__main__':
    sample_data = {
        "apple": 10,
        "banana": 20,
        "cherry": 30,
        "date": 40,
        "elderberry": 50
    }
    keys_to_validate = ["apple", "banana", "grape"]
    start_time = timeit.default_timer()
    result = validate_keys_against_dict(sample_data, keys_to_validate)
    end_time = timeit.default_timer()
    print(f"Validation Result: {result}")
    print(f"Execution Time (single run): {(end_time - start_time) * 10**6:.2f} microseconds")