import timeit
def validate_keys_against_dict(d: dict, keys_to_check: list) -> bool:
    return all(key in d for key in keys_to_check)
if __name__ == '__main__':
    sample_data = {'alpha': 10, 'beta': 20, 'gamma': 30}
    test_keys_1 = ['alpha', 'beta']
    test_keys_2 = ['delta', 'epsilon']
    iterations = 50000
    time_taken = timeit.timeit(
        stmt=f"validate_keys_against_dict({sample_data!r}, {test_keys_1!r})", 
        setup="from __main__ import validate_keys_against_dict, sample_data", 
        number=iterations
    )
    print(f"Validation of keys {test_keys_1} took: {time_taken:.4f}s")
    result = validate_keys_against_dict(sample_data, test_keys_2)
    print(f"Keys {test_keys_2} present in dictionary: {result}")