def is_odd(n):
    return n & 1 != 0
def check_number(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
if __name__ == '__main__':
    test_values = [5, -3, 10, 42]
    for val in test_values:
        check_number(val)