def enumerate_container(container):
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
    sample_data = [10, "hello", 3.14, None]
    output = enumerate_container(sample_data)
    for item in output:
        print(item)