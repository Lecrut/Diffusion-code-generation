def get_last_value(container, default=None):
    if not container:
        return default
    try:
        return container[-1]
    except (IndexError, TypeError):
        return default
if __name__ == '__main__':
    test_cases = [
        ([], "empty_list"),
        ("", "empty_string"),
        ([42, 30, 69], "list_with_ints"),
        (("a", "b", "c"), "tuple_of_chars"),
        (["x"], "single_element_list"),
    ]
    for container, name in test_cases:
        result = get_last_value(container)
        print(f"{name}: {result}")