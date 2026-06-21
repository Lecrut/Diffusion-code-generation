def evaluate_nested_logic(a, b, c, d):
    term_one = a and b
    term_two = c and (not d)
    return term_one or term_two

if __name__ == '__main__':
    result = evaluate_nested_logic(True, False, True, False)
    print(result)