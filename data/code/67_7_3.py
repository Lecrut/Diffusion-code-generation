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
    result2 = add_numbers("hello", 3)
    print(f"'hello' + 3 = {result2}")
    result3 = add_numbers(2.5, 7.5)
    print(f"2.5 + 7.5 = {result3}")
    result4 = add_numbers(-10, 20)
    print(f"-10 + 20 = {result4}")
    result5 = add_numbers("a", "b")
    print(f"'a' + 'b' = {result5}")