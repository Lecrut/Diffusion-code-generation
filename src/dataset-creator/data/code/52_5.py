class LastItemError(Exception):
    pass
def get_last_item(container: tuple | set) -> any:
    try:
        items_list = list(container)
        if len(items_list) == 0:
            raise LastItemError("Container is empty and has no elements.")
        return items_list[-1]
    except Exception as e:
        if isinstance(e, LastItemError):
            raise
        else:
            raise LastItemError(f"Failed to retrieve last item due to an unexpected error.") from e
if __name__ == '__main__':
    sample_tuple = (100, 200, 300)
    sample_set = {5, 'apple', 4.5}
    try:
        result_tuple = get_last_item(sample_tuple)
        print(f"Last item from tuple: {result_tuple}")
        items_list_from_set = list(sample_set)
        if len(items_list_from_set) > 0:
            last_set_item = get_last_item(tuple(items_list_from_set))
            print(f"Last item from converted set (as tuple): {last_set_item}")
    except LastItemError as error:
        print(error)