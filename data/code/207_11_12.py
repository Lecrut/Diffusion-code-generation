def locate_maximum(iterable):
    if not iterable:
        raise ValueError("Input iterable cannot be empty")
    return max(iterable, key=lambda x: x)

if __name__ == '__main__':
    sample_data = [7, 3, 9, 2, 5, 1]
    maximum_value = locate_maximum(sample_data)
    print(maximum_value)