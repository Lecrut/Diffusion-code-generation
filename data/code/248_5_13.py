def add_integers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    try:
        result = add_integers(3, 5)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")