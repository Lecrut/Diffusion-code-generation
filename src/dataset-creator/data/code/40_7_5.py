import timeit
def validate_keys_against_dict(dictionary: dict, keys_to_check: list) -> bool:
    return all(key in dictionary for key in keys_to_check)
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20, 'cherry': 30}
    test_keys = ['apple', 'banana']
    time_taken = timeit.timeit(
        stmt=f"validate_keys_against_dict({sample_data!r}, {test_keys!r})", 
        number=10000, 
        globals=globals()
    )
    result = validate_keys_against_dict(sample_data, test_keys)