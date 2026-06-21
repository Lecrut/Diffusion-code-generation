import math

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    num1 = 15
    num2 = 3
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    try:
        print("Division:", divide(num1, num2))
    except ValueError as e:
        print(e)

    circle = Circle(7.0)
    print(f"The area of a circle with radius {circle.radius} is: {circle.area()}")