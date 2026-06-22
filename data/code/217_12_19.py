NUMBERS = (10, 5)

def perform_operations(x, y):
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    division = None if y == 0 else x / y
    modulus = None if y == 0 else x % y
    return addition, subtraction, multiplication, division, modulus

if __name__ == '__main__':
    add, sub, mul, div, mod = perform_operations(*NUMBERS)
    print(f"Addition: {add}, Subtraction: {sub}, Multiplication: {mul}, Division: {div}, Modulus: {mod}")