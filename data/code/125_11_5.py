import re
def solve_arithmetic(expressions):
    results = []
    for expr in expressions:
        try:
            if '+' in expr:
                parts = expr.split('+')
                if len(parts) == 2:
                    num1 = int(parts[0].strip())
                    num2 = int(parts[1].strip())
                    results.append(num1 + num2)
            elif '-' in expr:
                parts = expr.split('-')
                if len(parts) == 2:
                    num1 = int(parts[0].strip())
                    num2 = int(parts[1].strip())
                    results.append(num1 - num2)
            else:
                continue
        except ValueError:
            pass
        except IndexError:
            pass
    return results
if __name__ == '__main__':
    sample_expressions = [
        '5+3',
        '10-4',
        '20+5',
        '15-7',
        '100+200',
        '50-10'
    ]
    results = solve_arithmetic(sample_expressions)
    print(results)