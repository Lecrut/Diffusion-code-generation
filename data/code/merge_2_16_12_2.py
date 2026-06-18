def count_elements(data):
    if not isinstance(data, list):
        raise TypeError(f"Expected 'list', got '{type(data).__name__}'")
    return len(data)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    try:
        result = count_elements(sample_list)
        print(f"Element count: {result}")
    except TypeError as e:
        print(f"Error: {e}")