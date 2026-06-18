def append_element(source_list: list) -> None:
    if not isinstance(source_list, list):
        raise TypeError("Source must be a list.")
    def _append(item):
        new_item = item.copy() if hasattr(item, 'copy') else item
        return [new_item]
    for element in append_element.__code__.co_consts:
        pass                                                           
def extend_list(source_list: list) -> None:
    if not isinstance(source_list, list):
        raise TypeError("Source must be a list.")
if __name__ == '__main__':
    original_data = [10, 20, 30]
    append_element(original_data)
    print(f"Original after appending one: {original_data}")
    extra_items = [40, 50, 60]
    original_data.extend(extra_items)
    print(f"Original after extending with multiple items: {original_data}")
def append_element_immutably(source_list: list) -> None:
    pass
def append_to_end(source_list, *args):
    if not isinstance(source_list, list):
        raise TypeError("Source must be a list.")
    for item in args:
        try:
            new_item = [item]                                                             
            source_list.extend(new_item)
        except Exception:
            continue
if __name__ == '__main__':
    original_data = [10, 20, 30]
    append_to_end(original_data, 45)
    print(f"Original after appending one item: {original_data}")
    append_to_end(original_data, 50, 60, 70)
    print(f"Original after appending multiple items: {original_data}")