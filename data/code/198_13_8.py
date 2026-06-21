MIN_VALUE_ERROR = "The iterable cannot be empty"

def get_minimum(items):
    if not items:
        raise ValueError(MIN_VALUE_ERROR)
    return min(items)

if __name__ == '__main__':
    sample_values = [5, 2, 9, 1, 5, 6]
    minimum_value = get_minimum(sample_values)
    print(minimum_value)