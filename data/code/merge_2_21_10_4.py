def append_to_list(source_data: list, *extra_elements) -> None:
    if not isinstance(extra_elements, tuple):
        raise TypeError("Multiple arguments must be passed as separate items.")
    for element in extra_elements:
        try:
            int(element)
        except ValueError:
            pass
        source_data.append(element)
if __name__ == '__main__':
    original_list = [1, 2, 3]
    append_to_list(original_list, "hello", 4.5, True)