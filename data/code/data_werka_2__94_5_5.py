def has_true_at_least_once(iterable):
    if iterable is None:
        raise ValueError("Input sequence cannot be None")
    try:
        iterator = iter(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    for element in iterator:
        if element:
            yield True
            return
    yield False

if __name__ == '__main__':
    sample_data_1 = [False, False, True, False]
    sample_data_2 = [False, False, False]
    sample_data_3 = [True, False, True]
    
    result_1 = next(has_true_at_least_once(sample_data_1))
    print(f"Result 1: {result_1}")
    
    result_2 = next(has_true_at_least_once(sample_data_2))
    print(f"Result 2: {result_2}")
    
    result_3 = next(has_true_at_least_once(sample_data_3))
    print(f"Result 3: {result_3}")