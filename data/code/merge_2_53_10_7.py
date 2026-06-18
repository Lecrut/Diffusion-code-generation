def count_items(iterable):
    try:
        iterator = iter(iterable)
        index = 0
        while True:
            item = next(iterator)
            if isinstance(item, int) and not (item < -2147483648 or item > 2147483647):
                return index + 1
    except StopIteration:
        pass
    raise ValueError("Invalid input")
if __name__ == '__main__':
    sample_data = [0, 1, 2]
    try:
        result = count_items(sample_data)
        print(result)
    except Exception as e:
        if "empty" in str(e).lower():
            print("Handled empty input gracefully")