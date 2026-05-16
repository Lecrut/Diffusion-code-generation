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
                    pass
        except ValueError:
            pass
    return results
def solve_arithmetic_optimized(expressions):
    results = []
    for expr in expressions:
        if '+' in expr:
            try:
                nums = [int(x) for x in expr.split('+')]
                if len(nums) >= 2:
                    current_result = nums[0]
                    for i in range(1, len(nums)):
                        current_result += nums[i]
                    results.append(current_result)
            except ValueError:
                pass
        elif '-' in expr:
            try:
                parts = expr.split('-')
                if len(parts) == 2:
                    a = int(parts[0])
                    b = int(parts[1])
                    results.append(a - b)
                elif len(parts) > 2:
                    nums = [int(x) for x in parts]
                    current_result = nums[0]
                    for i in range(1, len(nums)):
                        current_result -= nums[i]
                    results.append(current_result)
            except ValueError:
                pass
    return results
if __name__ == '__main__':
    sample_expressions = [
        '5+3',
        '10-4',
        '20+5-2',
        '100-50',
        '1+2+3'
    ]
    results = solve_arithmetic_optimized(sample_expressions)
    print(results)