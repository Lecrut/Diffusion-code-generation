def any_true_generator(seq):
    if not hasattr(seq, '__iter__'):
        raise ValueError("Input must be an iterable sequence of booleans")
    
    found = False
    for item in seq:
        if not isinstance(item, bool):
            raise ValueError("All items in the sequence must be boolean")
        if item:
            yield True
            found = True
            return
    
    if not found:
        yield False

if __name__ == '__main__':
    sample1 = [False, False, True, False]
    result1 = list(any_true_generator(sample1))
    print(f"Result for {sample1}: {result1}")

    sample2 = [False, False, False]
    result2 = list(any_true_generator(sample2))
    print(f"Result for {sample2}: {result2}")

    sample3 = [True, False, True]
    result3 = list(any_true_generator(sample3))
    print(f"Result for {sample3}: {result3}")

    sample4 = []
    result4 = list(any_true_generator(sample4))
    print(f"Result for {sample4}: {result4}")