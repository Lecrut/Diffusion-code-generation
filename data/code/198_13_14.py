def get_minimum(items):
    if not items:
        raise ValueError("The iterable cannot be empty")
    return min(items)

if __name__ == '__main__':
    sample_values = [15, 3, 8, 22, 1]
    minimum_value = get_minimum(sample_values)
    print(minimum_value)