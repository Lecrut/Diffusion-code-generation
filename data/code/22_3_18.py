# Check if an integer is odd using a single expression: num % 2 != 0
is_odd = lambda n: n % 2 != 0

if __name__ == '__main__':
    num = 17
    result = is_odd(num)
    print(f"The number {num} is {'odd' if result else 'even'}.")