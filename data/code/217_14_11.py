OUTCOME_EQUAL = 'Equal'
OUTCOME_GREATER = 'Greater'
OUTCOME_LESS = 'Less'

def compare_numbers(a, b):
    if a == b:
        return OUTCOME_EQUAL
    elif a > b:
        return OUTCOME_GREATER
    else:
        return OUTCOME_LESS
if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = compare_numbers(num1, num2)
    print(result)
    num3 = -3
    num4 = 7
    result2 = compare_numbers(num3, num4)
    print(result2)
    num5 = 42
    num6 = 42
    result3 = compare_numbers(num5, num6)
    print(result3)