import sys
def sort_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    print(*numbers)
if __name__ == '__main__':
    num1 = 5
    num2 = 1
    num3 = 3
    sort_numbers(num1, num2, num3)