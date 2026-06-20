def evaluate_and_operation(a, b):
    return a & b

if __name__ == '__main__':
    result = evaluate_and_operation(True, False)
    print(f"True AND False = {result}")