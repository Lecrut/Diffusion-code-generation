import marshal
import types

def get_code_object(func):
    return func.__code__

def check_equivalence(func1, func2):
    code1 = get_code_object(func1)
    code2 = get_code_object(func2)
    if code1.co_code != code2.co_code:
        return False
    sample_values = [0, 1]
    for val1 in sample_values:
        for val2 in sample_values:
            result1 = func1(val1, val2)
            result2 = func2(val1, val2)
            if result1 != result2:
                return False
    return True
if __name__ == '__main__':
    lambda1 = lambda x, y: x + y
    lambda2 = lambda x, y: y + x
    print(check_equivalence(lambda1, lambda2))