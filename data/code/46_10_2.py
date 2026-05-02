import sys
def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return None
    return a + b + c
if __name__ == '__main__':
    a = 5
    b = 12
    c = 13
    perimeter = calculate_perimeter(a, b, c)
    if perimeter is not None:
        print(perimeter)