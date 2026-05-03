import sys
def calculate_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle: The side lengths do not form a valid triangle."
    return a + b + c
if __name__ == '__main__':
    a = 3
    b = 4
    c = 5
    result = calculate_perimeter(a, b, c)
    print(result)