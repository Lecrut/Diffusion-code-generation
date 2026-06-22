MAX_FLOAT = float('inf')

def find_largest(a, b, c):
    largest = max(a, b, c)
    return largest

if __name__ == '__main__':
    num1 = 3.5
    num2 = 7.8
    num3 = 2.4
    print(f"Largest number among {num1}, {num2}, and {num3} is: {find_largest(num1, num2, num3)}")