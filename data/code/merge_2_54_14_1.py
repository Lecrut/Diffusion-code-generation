def find_middle_index(items):
    if not isinstance(items, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    length = len(items)
    return length // 2
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    middle_index = find_middle_index(sample_data)
    print(f"Middle index: {middle_index}")