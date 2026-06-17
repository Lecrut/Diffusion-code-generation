import timeit
def validate_keys(d: dict) -> list[str]:
    return [key for key in d.keys() if isinstance(key, str)]
if __name__ == '__main__':
    sample_dict = {'apple': 10, 'banana': 20, 'cherry': 30}
    test_keys = ['apple', 'orange', 'grape']
    start_time = timeit.default_timer()
    results = validate_keys(sample_dict)
    end_time = timeit.default_timer()
    print(f"Validated keys: {results}")