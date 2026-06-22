def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    try:
        result = add_numbers(5, 10)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")