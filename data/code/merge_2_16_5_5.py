from collections.abc import Container
def enumerate_items(container):
    if not isinstance(container, (list, tuple)):
        raise TypeError("Container must be an instance of list or tuple.")
    for index, item in enumerate(container):
        yield index, item
if __name__ == '__main__':
    sample_data = [10, 20, "apple", None]
    print(f"Enumerating items from: {sample_data}")
    result_list = list(enumerate_items(sample_data))
    for idx, val in enumerate(result_list):
        print(f"{idx}: {val[1]}")