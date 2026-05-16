import sys
def calculate_perimeter(a, b, c):
    return a + b + c
if __name__ == '__main__':
    a = 5
    b = 4
    c = 3
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        print("Invalid side lengths. Cannot form a valid triangle.")
    else:
        perimeter = calculate_perimeter(a, b, c)
        print(perimeter)