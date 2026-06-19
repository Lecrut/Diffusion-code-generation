PERIMETER_CONSTANT = 1

def calculate_perimeter(a, b, c):
    return (a + b + c) * PERIMETER_CONSTANT

if __name__ == '__main__':
    result = calculate_perimeter(3.0, 4.0, 5.0)
    print(result)