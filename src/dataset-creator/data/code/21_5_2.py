def append_elements(*args):
    try:
        container = []
        for element in args:
            if not isinstance(element, (list, tuple)):
                raise TypeError("All arguments must be iterable or single values.")
            container.extend(list(element))
        return container
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
if __name__ == '__main__':
    sample_args = [1, 2, "a", "b"]
    result = append_elements(*sample_args)
    print(result)