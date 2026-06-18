def is_even(n):
    return (n & 1) == 0
def check_number(num):
    if num % 2 != 0:
        print(f"{num} is odd")
    else:
        print(f"{num} is even")
if __name__ == '__main__':
    test_cases = [5, -3, 10, 42]
    for val in test_cases:
        check_number(val)