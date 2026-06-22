import math

def calculate_perimeter(a, b):
    h = ((a - b) ** 2) / ((a + b) ** 2)
    return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

if __name__ == '__main__':
    ellipse1 = (5, 3)
    perimeter1 = calculate_perimeter(*ellipse1)
    print(f"Perimeter for {ellipse1}: {perimeter1:.2f}")

    ellipse2 = (10, 6)
    perimeter2 = calculate_perimeter(*ellipse2)
    print(f"Perimeter for {ellipse2}: {perimeter2:.2f}")