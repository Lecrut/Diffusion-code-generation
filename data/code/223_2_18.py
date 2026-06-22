def find_max(iterable):
    max_value = None
    for value in iterable:
        if max_value is None or value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_values = [10, 23, 5, 78, 45]
    print(f"Maximum of {sample_values}: {find_max(sample_values)}")