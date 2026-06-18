def count_elements(collection):
    try:
        if not hasattr(collection, "__iter__"):
            raise TypeError("Input must be iterable")
        counter = 0
        for _ in collection:
            counter += 1
        return counter
    except Exception as e:
        print(f"Error during iteration: {e}")
        return None
if __name__ == '__main__':
    sample_data = [1, 'a', True]
    result = count_elements(sample_data)
    if isinstance(result, int):
        print(f"Count of elements: {result}")