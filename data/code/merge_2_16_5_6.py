import collections
def enumerate_items(container):
    if not isinstance(container, (list, tuple)):
        raise TypeError("Container must be a list or tuple.")
    for index, item in enumerate(container):
        yield f"{index}: {item}"
if __name__ == '__main__':
    sample_data = [10, "hello", 3.14]
    result_list = []
    for line in enumerate_items(sample_data):
        result_list.append(line)
    print("\n".join(result_list))