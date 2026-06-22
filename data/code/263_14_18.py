MAX_FLOAT = float('inf')

def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    num1 = 3.5
    num2 = 7.2
    num3 = 4.8
    largest = find_largest(num1, num2, num3)
    print(f"The largest number is: {largest}")