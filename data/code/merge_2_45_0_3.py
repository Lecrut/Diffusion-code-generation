def add_numbers(a: int, b: int) -> None:
    try:
        result = a + b
        print(f"Sum is {result}")
    except TypeError as e:
        if isinstance(e.__cause__, ValueError):
            raise
        else:
            print("Error:", str(e))
if __name__ == '__main__':
    add_numbers(5, 10)