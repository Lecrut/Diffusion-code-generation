def evaluate_logic(a: bool, b: bool) -> bool:
    c = a or not b
    return (a and b) or (not a and c)

if __name__ == '__main__':
    result = evaluate_logic(True, False)
    print(result)