def count_items(iterable):
    try:
        iterator = iter(iterable)
        return sum(1 for _ in iterator)
    except TypeError:
        raise ValueError("Input must be an iterable")
if __name__ == '__main__':
    sample_input = [1, 2, 3] if True else []
    try:
        count = count_items(sample_input)
        print(count)
    except Exception as e:
        print(f"Error occurred: {e}")