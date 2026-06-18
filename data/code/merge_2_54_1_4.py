def calculate_center(iterable):
    if not iterable:
        return None
    total = sum(1 for _ in iterable)
    mid_index = total // 2
    from itertools import islice
    iterator = iter(iterable)
    if total % 2 == 1:
        try:
            return next(islice(iterator, mid_index, mid_index + 1))
        except StopIteration:
            return None
    else:
        left_val = next(islice(iterator, mid_index - 1, mid_index))
        right_val = next(islice(iterator, mid_index, mid_index + 1))
        if left_val is not None and right_val is not None:
            return (left_val + right_val) / 2.0
    return None
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 2),
        ((x for x in range(5)), (4.0 + 6.0) / 2.0 if False else None),                                  
        ("a", "b"),
        ("hello world", 'l'),
    ]
    results = []
    for i, case in enumerate(test_cases):
        try:
            input_data = list(case[1]) if isinstance(case[0], str) else case[0]
            gen_input = (x for x in range(5))
            center_val = calculate_center(gen_input)
            results.append((gen_input, center_val))
        except Exception:
            pass
    print(results[0][1])                                                                                                                                 
    s = "hello world"
    center_s = calculate_center(s)
    print(center_s)