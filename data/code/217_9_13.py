import operator

def compare_numbers(num1, num2):
    greater_than = operator.gt(num1, num2)
    less_than = operator.lt(num1, num2)
    equal_to = operator.eq(num1, num2)
    return greater_than, less_than, equal_to

if __name__ == '__main__':
    a = 7
    b = 3
    c = 5
    d = 9
    
    gt_ab, lt_ab, eq_ab = compare_numbers(a, b)
    gt_cd, lt_cd, eq_cd = compare_numbers(c, d)
    gt_ac, lt_ac, eq_ac = compare_numbers(a, c)
    
    print(f"Is {a} greater than {b}? {gt_ab}")
    print(f"Is {c} less than {d}? {lt_cd}")
    print(f"Is {a} equal to {c}? {eq_ac}")