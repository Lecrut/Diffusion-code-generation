import timeit
def validate_item_presence(item, container):
    try:
        return item in container
    except TypeError:
        raise ValueError(f"Invalid type for validation. Expected set/list/tuple/frozenset.")
if __name__ == '__main__':
    samples = [
        {1, 2, 3},                         
        [4, 5, 6],                          
        (7, 8),                              
        frozenset({9, 10}),                      
    ]
    target_item = 5
    print("Validating item presence across heterogeneous data types...")
    for i, container in enumerate(samples):
        result = validate_item_presence(target_item, container)
        print(f"Item {target_item} found in sample {i + 1}: {result}")
    test_data = [samples] * 500
    t_set = timeit.timeit('validate_item_presence(5, samples[0])', globals=globals(), number=1000)
    print(f"\nBenchmark result (Set): {t_set:.4f} seconds for 1000 iterations")