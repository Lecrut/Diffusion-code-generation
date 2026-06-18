def add_numbers():
    try:
        num1 = int(5)
        num2 = 3
        return num1 + num2
    except ValueError as e:
        print(f"Error: {e}")
        raise
if __name__ == '__main__':
    result = add_numbers()
    print(result)