BITWISE_OR = lambda x, y: x | y

def check_conditions(*conditions):
    return any(conditions)
if __name__ == '__main__':
    condition1 = lambda x: x > 0
    condition2 = lambda x: x % 2 == 0
    result = check_conditions(condition1(5), condition2(4))
    print(result)