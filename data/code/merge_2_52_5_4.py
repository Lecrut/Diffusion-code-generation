class ContainerError(Exception):
    pass
def get_last_item(container: tuple | list | set) -> any:
    supported_types = (tuple, list)
    if isinstance(container, supported_types):
        return container[-1]
    elif isinstance(container, set):
        if not container:
            raise ContainerError("Cannot retrieve last item from an empty set.")
        return list(container)[-1] if container else None
    raise ContainerError(f"Unsupported container type: {type(container).__name__}. Only tuple, list, and set are supported.")
if __name__ == '__main__':
    ordered_list = [50, 49, 38]
    ordered_tuple = ('apple', 'banana')
    empty_set = set()
    try:
        result1 = get_last_item(ordered_list)
        print(f"Last item in list {ordered_list}: {result1}")
        result2 = get_last_item(ordered_tuple)
        print(f"Last item in tuple {ordered_tuple}: {result2}")
        non_empty_set = {'a', 'b', 'c'}
        try:
            result3 = get_last_item(non_empty_set)
            print(f"Arbitrary last item from set {non_empty_set}: {result3}")
            result4 = get_last_item(empty_set)
        except ContainerError as e:
            print(f"Expected error for empty container: {e}")
    except Exception as ex:
        print(f"Unexpected error occurred: {ex}")