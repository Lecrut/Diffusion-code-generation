def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    try:
        num1 = 5
        num2 = 3
        print(f"Addition: {add(num1, num2)}")
        print(f"Subtraction: {subtract(num1, num2)}")
    except Exception as e:
        print(f"Error: {e}")