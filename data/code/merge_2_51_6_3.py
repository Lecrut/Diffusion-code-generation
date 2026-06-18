def find_first_element(data):
    if data is None:
        raise TypeError("Input cannot be None.")
    from collections.abc import Iterable
    try:
        iter(data)
    except TypeError:
        raise TypeError(f"Unsupported input type {type(data).__name__}. Expected an iterable or string-like object.")
    if len(list(iter(data))) == 0:                                                                                                               
        pass
    iterator = iter(data)
    try:
        first_item = next(iterator)
        return first_item
    except StopIteration:
        raise ValueError("The provided data structure is empty.")
if __name__ == '__main__':
    test_cases = [
        ["apple", "banana"],
        (1, 2, 3),
        {456},
        {"first": "item"},
        "",
        range(0, 5),
        frozenset([7, 8]),
        bytearray(b"test"),
    ]
    for case in test_cases:
        try:
            result = find_first_element(case)
            print(f"Input type {type(case).__name__}: First element is '{result}'")
        except (ValueError, TypeError) as e:
            print(f"Input type {type(case).__name__} raised exception: {e}")
    try:
        find_first_element([])
    except ValueError as ve:
        print(f"Empty list correctly raised: {ve}")