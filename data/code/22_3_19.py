# Check if 'num' is odd using single-line expression with bitwise AND operator: num & 1 != 0
if __name__ == '__main__':
    num = 17
    result = "Odd" if (num % 2) else "Even"
    print(f"{num} is {result}")