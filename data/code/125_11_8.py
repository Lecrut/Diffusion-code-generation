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
            elif len(parts) == 2 and expr.count('-') == 1:
                num1 = int(parts[0])
                num2 = int(parts[1])
                results.append(num1 - num2)
            elif len(parts) == 1 and '-' in expr:
                parts_sub = expr.split('-')
                num1 = int(parts_sub[0])
                num2 = int(parts_sub[1])
                results.append(num1 - num2)
            else:
                raise ValueError("Invalid format")
        except ValueError:
            results.append(f"Error processing: {expr}")
        except Exception:
            results.append(f"Error processing: {expr}")
    return results
if __name__ == '__main__':
    sample_expressions = ['5+3', '10-4', '20+5', '15-7', '100+100']
    results = solve_arithmetic(sample_expressions)
    print(results)