def evaluate_expression(expression):
    results = {}
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                input_tuple = (a, b, c)
                result = eval(expression, {'A': a, 'B': b, 'C': c})
                results[input_tuple] = result
    return results

if __name__ == '__main__':
    expression = "A and B or C"
    print(evaluate_expression(expression))