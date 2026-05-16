import re
def solve_arithmetic(expressions):
    results = []
    for expr in expressions:
        try:
            parts = expr.split('+')
            if len(parts) == 2:
                num1 = int(parts[0])
                num2 = int(parts[1])
                results.append(num1 + num2)
            elif len(parts) == 2 and '-' in expr:
                parts_sub = expr.split('-')
                num1 = int(parts_sub[0])
                num2 = int(parts_sub[1])
                results.append(num1 - num2)
            elif len(parts) == 3 and '-' in expr:
                parts_sub = expr.split('-')
                num1 = int(parts_sub[0])
                num2 = int(parts_sub[1])
                num3 = int(parts_sub[2])
                results.append(num1 - num2 - num3)
            elif len(parts) == 3 and '+' in expr:
                parts_add = expr.split('+')
                num1 = int(parts_add[0])
                num2 = int(parts_add[1])
                num3 = int(parts_add[2])
                results.append(num1 + num2 + num3)
            elif len(parts) == 3 and '-' in expr:
                parts_sub = expr.split('-')
                num1 = int(parts_sub[0])
                num2 = int(parts_sub[1])
                num3 = int(parts_sub[2])
                results.append(num1 - num2 - num3)
            elif len(parts) == 3 and '+' in expr and '-' in expr:
                pass
            else:
                if '-' in expr:
                    try:
                        a, b = map(int, expr.split('-'))
                        results.append(a - b)
                    except ValueError:
                        pass
                else:
                    try:
                        a, b = map(int, expr.split('+'))
                        results.append(a + b)
                    except ValueError:
                        pass
        except ValueError:
            continue
        except Exception:
            continue
    return results
if __name__ == '__main__':
    test_expressions = [
        '5+3',
        '10-4',
        '20+5-1',
        '15-7',
        '10+2+3',
        '20-10-5'
    ]
    results = solve_arithmetic(test_expressions)
    print(results)