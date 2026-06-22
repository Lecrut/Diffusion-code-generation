def check_first_true(sequence):
    if sequence is None:
        raise ValueError("Input sequence cannot be None")
    
    def _validate_element(item):
        if not isinstance(item, bool):
            raise ValueError(f"Expected boolean, got {type(item).__name__}")
        return item
    
    for item in sequence:
        _validate_element(item)
        if item:
            yield True
            return

if __name__ == '__main__':
    data1 = [False, False, True, False]
    gen1 = check_first_true(data1)
    res1 = next(gen1, False)
    print(f"First True in {data1}: {res1}")
    
    data2 = [False, False, False]
    gen2 = check_first_true(data2)
    res2 = next(gen2, False)
    print(f"First True in {data2}: {res2}")
    
    data3 = [True, False, True]
    gen3 = check_first_true(data3)
    res3 = next(gen3, False)
    print(f"First True in {data3}: {res3}")
    
    data4 = []
    gen4 = check_first_true(data4)
    res4 = next(gen4, False)
    print(f"First True in {data4}: {res4}")