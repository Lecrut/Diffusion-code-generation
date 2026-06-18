import timeit
def validate_keys(d: dict, keys_to_check: list) -> bool:
    return all(key in d for key in keys_to_check)
if __name__ == '__main__':
    sample_dictionary = {
        'alpha': 10,
        'beta': 20.5,
        'gamma': [3, 4, 5],
        'delta': {'nested': True}
    }
    keys_to_validate = ['alpha', 'nonexistent', 'beta']
    time_taken = timeit.timeit(
        stmt=f"validate_keys({sample_dictionary}, {keys_to_validate})", 
        number=10000, 
        globals=globals()
    )
    result = validate_keys(sample_dictionary, keys_to_validate)
    print(f"Validation Result: {result}")
    print(f"Time taken for 10k iterations: {time_taken:.4f} seconds")