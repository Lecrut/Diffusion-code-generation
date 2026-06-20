def evaluate_and_operation(bool1, bool2):
    return bool1 & bool2

if __name__ == '__main__':
    result = evaluate_and_operation(True, False)
    print(f"True AND False = {result}")