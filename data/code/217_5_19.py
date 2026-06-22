def compare(a: float, b: float) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    return (a > b) - (a < b)
if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(compare(num1, num2))
    num1 = 10
    num2 = 10
    print(compare(num1, num2))
    num1 = 1
    num2 = 5
    print(compare(num1, num2))