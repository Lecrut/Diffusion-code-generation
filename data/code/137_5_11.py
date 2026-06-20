def get_max(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a if a > b else b

if __name__ == '__main__':
    print(get_max(5, 3))