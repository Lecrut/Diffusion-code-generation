def get_first_item(item_list):
    if item_list is None:
        return "Input cannot be null"
    try:
        first = next(iter(item_list))
        return first
    except StopIteration:
        pass
    raise ValueError("The list provided was empty.")
if __name__ == '__main__':
    sample_cases = [
        ["apple", "banana"],
        [],
        None,
        {"a": 1},
        set([10]),
        {1: 'one'}
    ]
    for case in sample_cases:
        try:
            result = get_first_item(case)
            print(f"Input type: {type(case).__name__} -> Result: {result}")
        except ValueError as e:
            print(f"Input type: {type(case).__name__} -> Error: {e}")