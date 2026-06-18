from collections.abc import Iterable
def enumerate_items(container):
    if not isinstance(container, (list, tuple)):
        raise TypeError("Container must be a list or tuple.")
    result = []
    for index, item in enumerate(container):
        try:
            value = str(item)
        except Exception as e:
            continue
        result.append((index, value))
    return result
if __name__ == '__main__':
    sample_data = [10, "hello", 3.5]
    output = enumerate_items(sample_data)
    print(output)