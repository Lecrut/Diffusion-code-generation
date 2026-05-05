def add_numbers(a, b):
    try:
        num1 = float(a)
        num2 = float(b)
        return num1 + num2
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
if __name__ == '__main__':
    result1 = add_numbers(10, 5)
    print(f"10 + 5 = {result1}")
    result2 = add_numbers("hello", 5)
    print(f"'hello' + 5 = {result2}")
    result3 = add_numbers(3.5, 2.1)
    print(f"3.5 + 2.1 = {result3}")
    result4 = add_numbers("a", "b")
    print(f"'a' + 'b' = {result4}")