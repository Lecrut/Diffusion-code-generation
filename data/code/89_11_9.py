def evaluate_and_operation(num1, num2):
    return bool(num1 & num2)

if __name__ == '__main__':
    result = evaluate_and_operation(10, 5)
    print(f"10 AND 5 = {result}")