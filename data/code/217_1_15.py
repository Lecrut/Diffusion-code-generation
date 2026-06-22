def compare_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return a > b

if __name__ == '__main__':
    print(compare_numbers(10, 5))
    print(compare_numbers(20, 30))
    try:
        print(compare_numbers(7, "7"))
    except ValueError as e:
        print(e)