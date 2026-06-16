def append_element(container: list | tuple, element) -> None:
    if isinstance(container, (list, tuple)):
        try:
            container = list(container)
            container.append(element)
        except Exception as e:
            raise TypeError(f"Invalid operation on {type(container).__name__}: {e}") from e
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    append_element(sample_list, "new_item")
    append_element(sample_tuple, "another_new_item")