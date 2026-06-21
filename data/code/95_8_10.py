def check_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if n <= 0:
        return "Number is not positive"
    if n % 2 != 0:
        return "Number is odd"
    if n >= 100:
        return "Number is greater than or equal to 100"
    return "Number is positive, even, and less than 100"

if __name__ == '__main__':
    print(check_number(50))
    print(check_number(-5))
    print(check_number(101))
    print(check_number(51))