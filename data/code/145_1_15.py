TRUE = True
FALSE = False

def evaluate_nested_logic(a, b, c):
    result = a and b or c
    return result
if __name__ == '__main__':
    sample_values = [(TRUE, FALSE, TRUE), (FALSE, TRUE, FALSE), (TRUE, TRUE, FALSE), (FALSE, FALSE, TRUE)]
    for a, b, c in sample_values:
        result = evaluate_nested_logic(a, b, c)
        print(f'evaluate_nested_logic({a}, {b}, {c}) = {result}')