def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_iterable = [3.14, 1.618, 2.718, 0.577, 9.999, -1.0, 5.0]
    try:
        maximum = find_maximum(sample_iterable)
        print(maximum)
    except ValueError as e:
        print(e)