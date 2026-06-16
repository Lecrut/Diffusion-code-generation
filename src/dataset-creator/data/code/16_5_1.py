from collections.abc import Iterable
def enumerate_container(container):
    if not isinstance(container, (list, tuple)):
        raise TypeError("Container must be an instance of list or tuple.")
    for index, item in enumerate(container):
        yield f"{index}: {item}"
if __name__ == '__main__':
    sample_data = [10, "apple", 3.5]
    print("\n".join(enumerate_container(sample_data)))