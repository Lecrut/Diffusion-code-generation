def add_numbers(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    result = add_numbers(10, 20)
    print(result)