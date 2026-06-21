def evaluate_nested_logic(a: bool, b: bool, c: bool) -> bool:
    return not (a and b or c)

if __name__ == '__main__':
    result = evaluate_nested_logic(True, False, True)
    print(result)