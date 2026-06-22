def evaluate_nested_logic(a, b, c, d):
    if a and b:
        return True
    if c and not d:
        return True
    return False

if __name__ == '__main__':
    result = evaluate_nested_logic(True, False, True, False)
    print(result)