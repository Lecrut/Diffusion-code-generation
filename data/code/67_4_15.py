def safe_sum(a, b):
    try:
        return a + b
    except TypeError as e:
        raise ValueError("Both inputs must be numbers") from e

if __name__ == '__main__':
    first_value = 15
    second_value = 25
    print(safe_sum(first_value, second_value))