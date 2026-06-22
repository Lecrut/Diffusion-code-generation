def add_two_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    try:
        result = add_two_numbers(5, 3)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")