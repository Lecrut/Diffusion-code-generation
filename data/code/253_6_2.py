import math
def find_middle(a, b, c):
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    middle = find_middle(num1, num2, num3)
    print(middle)