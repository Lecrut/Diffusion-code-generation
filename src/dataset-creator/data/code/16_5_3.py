from collections.abc import Container
def enumerate_container(container):
    if not isinstance(container, (list, tuple)):
        raise TypeError("Container must be a list or tuple.")
    result = []
    for item in container:
        try:
            str(item)
        except TypeError:
            continue
        result.append((item, len(result)))
    return result
if __name__ == '__main__':
    sample_data = [10, "hello", None, 3.14]
    output_list = enumerate_container(sample_data)
    print("Enumerated items:")
    for item, index in output_list:
        print(f"Index {index}: {item!r}")