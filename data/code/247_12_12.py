def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    try:
        result = add_numbers(5, 3)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")