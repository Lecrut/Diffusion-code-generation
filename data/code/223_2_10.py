def find_max_value(iterable):
    if not iterable:
        raise ValueError("Input iterable cannot be empty")
    max_val = iterable[0]
    for item in iterable[1:]:
        if item > max_val:
            max_val = item
    return max_val

if __name__ == '__main__':
    sample_data = [7, 3, 9, 1, 5]
    print(f"Maximum value in {sample_data}: {find_max_value(sample_data)}")