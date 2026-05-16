import re
def solve_arithmetic(expressions):
    results = []
    for expr in expressions:
        match = re.match(r"(\d+)\s*([+\-])\s*(\d+)", expr)
        if match:
            num1 = int(match.group(1))
            operator = match.group(2)
            num2 = int(match.group(3))
            if operator == '+':
                results.append(num1 + num2)
            elif operator == '-':
                results.append(num1 - num2)
    return results
if __name__ == '__main__':
    sample_expressions = [
        '5+3',
        '10-4',
        '20+7',
        '15-8',
        '100+50',
        '12-1'
    ]
    results = solve_arithmetic(sample_expressions)
    print(results)