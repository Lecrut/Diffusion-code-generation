import math
def find_middle(a, b, c):
    if (a <= b and b <= c) or (c <= b and b <= a):
        return b
    elif (b <= a and a <= c) or (c <= a and a <= b):
        return a
    else:
        return c
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 20
    middle = find_middle(num1, num2, num3)
    print(middle)