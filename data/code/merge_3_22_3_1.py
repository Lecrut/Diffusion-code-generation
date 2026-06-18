# Check if an integer is odd using bitwise AND with 1
is_odd = lambda n: (n & 1) == 1

if __name__ == '__main__':
    num = 17
    result = "Odd" if is_odd(num) else "Even"
    print(f"{num} is {result}")