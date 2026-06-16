from collections.abc import Iterable
def enumerate_items(container):
    if not isinstance(container, (list, tuple)):
        raise TypeError("Container must be a list or tuple.")
    result = []
    for index, item in enumerate(container):
        result.append((index, item))
    return result
if __name__ == '__main__':
    sample_data = [10, 20, "apple", None]
    output = enumerate_items(sample_data)
    print(output)