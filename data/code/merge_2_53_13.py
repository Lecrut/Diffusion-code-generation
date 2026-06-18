def count_elements(collection):
    try:
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        counter = 0
        for item in collection:
            counter += 1
        return counter
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
if __name__ == '__main__':
    sample_data = [1, 'a', True]
    result = count_elements(sample_data)
    if result is not None:
        print(result)