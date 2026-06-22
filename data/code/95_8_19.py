def check_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if n <= 0:
        return "Not positive"
    if n % 2 != 0:
        return "Not even"
    if n >= 100:
        return "Not less than 100"
    return "Positive, even, and less than 100"

if __name__ == '__main__':
    print(check_number(50))
    print(check_number(-10))
    print(check_number(7))
    print(check_number(100))