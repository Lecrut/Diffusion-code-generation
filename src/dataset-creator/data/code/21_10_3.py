def append_to_list(original_data: list, *elements) -> None:
    if not isinstance(elements, tuple):
        elements = (elements,)
    for item in elements:
        original_data.append(item)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    append_to_list(sample_list, "new", True, None, {"key": "value"})