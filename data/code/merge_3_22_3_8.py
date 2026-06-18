# Check if an integer is odd using a single expression
is_odd = lambda n: n % 2 != 0

if __name__ == '__main__':
    num = 17
    print(f"Is {num} odd? {is_odd(num)}")