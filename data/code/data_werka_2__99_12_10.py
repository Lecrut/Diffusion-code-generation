from functools import reduce
from operator import and_, or_, xor_

class FlagExpression:
    def __init__(self, left=None, right=None, op=None, value=None):
        if value is not None:
            self.value = value
            self.op = None
            self.left = None
            self.right = None
        else:
            self.left = left
            self.right = right
            self.op = op

    def evaluate(self, flags):
        if self.op is None:
            return bool(self.value & flags)
        
        if self.op == and_:
            left_val = self.left.evaluate(flags)
            if not left_val:
                return False
            return self.right.evaluate(flags)
        
        if self.op == or_:
            left_val = self.left.evaluate(flags)
            if left_val:
                return True
            return self.right.evaluate(flags)
        
        if self.op == xor_:
            return self.left.evaluate(flags) != self.right.evaluate(flags)
        
        raise ValueError(f"Unsupported operator: {self.op}")

def make_and(left, right):
    return FlagExpression(left=left, right=right, op=and_)

def make_or(left, right):
    return FlagExpression(left=left, right=right, op=or_)

def make_xor(left, right):
    return FlagExpression(left=left, right=right, op=xor_)

def make_flag(value):
    return FlagExpression(value=value)

def evaluate_expression(expr, flags):
    return expr.evaluate(flags)

if __name__ == '__main__':
    flag_a = make_flag(1)
    flag_b = make_flag(2)
    flag_c = make_flag(4)
    
    complex_expr = make_or(
        make_and(flag_a, flag_b),
        flag_c
    )
    
    result1 = evaluate_expression(complex_expr, 3)
    print(result1)
    
    result2 = evaluate_expression(complex_expr, 4)
    print(result2)
    
    result3 = evaluate_expression(complex_expr, 0)
    print(result3)
    
    xor_expr = make_xor(flag_a, flag_b)
    result4 = evaluate_expression(xor_expr, 3)
    print(result4)
    
    result5 = evaluate_expression(xor_expr, 1)
    print(result5)