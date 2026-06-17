class ContainerError(Exception):
    pass
def get_last_item(container: tuple | set) -> any:
    if not isinstance(container, (tuple, set)):
        raise ContainerError(f"Unsupported container type: {type(container).__name__}. Only tuple and set are supported.")
    try:
        if isinstance(container, set):
            container_list = list(container)
        else:
            container_list = list(container)
        if len(container_list) == 0:
            raise ContainerError("Container cannot be empty.")
        return container_list[-1]
    except Exception as e:
        error_msg = f"Failed to retrieve last item from {type(container).__name__}: {str(e)}"
        raise ContainerError(error_msg)
if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    sample_set = {'apple', 'banana', 'cherry'}
    try:
        last_from_tuple = get_last_item(sample_tuple)
        print(f"Last item from tuple {sample_tuple}: {last_from_tuple}")
        last_from_set = get_last_item(sample_set)
        print(f"Last item from set {sample_set} (arbitrary): {last_from_set}")
    except ContainerError as e:
        print(f"An error occurred: {e}")