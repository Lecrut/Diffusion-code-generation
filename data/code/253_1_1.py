import sys
def find_middle(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[1]
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 20
    result = find_middle(num1, num2, num3)
    print(result)