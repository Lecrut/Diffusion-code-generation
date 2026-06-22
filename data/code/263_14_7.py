def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    num1 = 3.5
    num2 = 7.8
    num3 = 2.9
    print(f"The largest number among {num1}, {num2}, and {num3} is: {find_largest(num1, num2, num3)}")