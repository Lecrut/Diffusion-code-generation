def add_two_numbers(a: float, b: float) -> float:
    return a + b

if __name__ == '__main__':
    try:
        num1 = 5.2
        num2 = 7.8
        result = add_two_numbers(num1, num2)
        print(result)
    except Exception as e:
        print(f"Error: {e}")