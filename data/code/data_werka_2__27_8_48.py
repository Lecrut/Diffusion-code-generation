def check_difference(a, b):
    try:
        return a != b
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    value1 = 42
    value2 = 43
    result = check_difference(value1, value2)
    print(result)