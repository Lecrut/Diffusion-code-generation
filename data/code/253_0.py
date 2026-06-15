import math
def find_middle(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[1]
if __name__ == '__main__':
    num1 = 5
    num2 = 1
    num3 = 8
    median = find_middle(num1, num2, num3)
    print(median)