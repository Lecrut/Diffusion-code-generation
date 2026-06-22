def find_maximum(iterable):
    if not iterable:
        raise ValueError("Input iterable cannot be empty")
    max_value = iterable[0]
    for item in iterable[1:]:
        if item > max_value:
            max_value = item
    return max_value

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(f"Maximum of {sample_values}: {find_maximum(sample_values)}")