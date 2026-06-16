import timeit
def validate_item_presence(item, container):
    try:
        return item in container
    except TypeError:
        raise ValueError(f"Cannot check presence of {type(item).__name__} in {type(container).__name__}")
if __name__ == '__main__':
    test_item = 42
    collections_to_test = [
        {"set": {1, 2, 3, 42}, "list": [10, 20, 30, 42], 
         "tuple": (50, 60, 70, 80), "frozenset": frozenset([90, 100])}
    ]
    test_data = [collections_to_test] * 10
    for collection_type in ["set", "list", "tuple"]:
        sample_collection = collections_to_test[0][collection_type] if collection_type != "frozenset" else collections_to_test[0]["frozenset"]
        iterations = 10000
        result_time = timeit.timeit(
            stmt=f'validate_item_presence({test_item}, {sample_collection})', 
            setup='from __main__ import validate_item_presence; test_item=42', 
            number=iterations
        )
        avg_time_per_call = result_time / iterations
        print(f"{collection_type.capitalize()} validation time: {avg_time_per_call:.6f} seconds per call")
    final_checks = [validate_item_presence(test_item, c) for c in collections_to_test[0].values()]
    if all(final_checks):
        print("All presence checks passed successfully.")
    else:
        print("Some presence checks failed unexpectedly.")