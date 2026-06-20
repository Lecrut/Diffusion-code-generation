import math
NUM1 = 25.5
NUM2 = 4.2

def calculate_operations(num1=NUM1, num2=NUM2):
    results = {'addition': num1 + num2, 'subtraction': num1 - num2, 'multiplication': num1 * num2, 'division': num1 / num2 if num2 != 0 else 'Division by zero error'}
    return results
if __name__ == '__main__':
    results = calculate_operations()
    print(results)