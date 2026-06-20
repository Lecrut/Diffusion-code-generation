def evaluate_and_operation(a, b):
    return bool(a & b)

if __name__ == '__main__':
    result = evaluate_and_operation(True, False)
    print(f"AND operation (True, False): {result}")