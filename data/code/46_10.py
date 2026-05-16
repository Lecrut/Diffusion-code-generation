import sys
def calculate_perimeter(a, b, c):
    return a + b + c
if __name__ == '__main__':
    a = 5
    b = 4
    c = 3
    if a > 0 and b > 0 and c > 0:
        perimeter = calculate_perimeter(a, b, c)
        print(perimeter)
    else:
        print("Error: Side lengths must be positive numbers.")