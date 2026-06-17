import timeit
def validate_keys_against_dict(data: dict, keys_to_check: list) -> bool:
    return all(key in data for key in keys_to_check)
if __name__ == '__main__':
    sample_data = {'alpha': 10, 'beta': 20, 'gamma': 30}
    test_keys_1 = ['alpha', 'beta']
    test_keys_2 = ['delta', 'epsilon']
    result_set_1 = validate_keys_against_dict(sample_data, test_keys_1)
    result_set_2 = validate_keys_against_dict(sample_data, test_keys_2)
    print(f"Keys {test_keys_1} present: {result_set_1}")
    print(f"Keys {test_keys_2} present: {result_set_2}")
    benchmark_time = timeit.timeit(
        stmt=f'validate_keys_against_dict({{"a": 1, "b": 2}}, ["a", "c"])',
        setup='from __main__ import validate_keys_against_dict',
        number=10000
    )
    print(f"Average execution time for 10k iterations: {benchmark_time:.6f} seconds")