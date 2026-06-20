def subtract_numbers(a: int, b: int) -> int:
    return a - b

if __name__ == '__main__':
    try:
        result = subtract_numbers(10, 5)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")