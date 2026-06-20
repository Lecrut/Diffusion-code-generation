LOGICAL_AND = lambda a, b: a and b
LOGICAL_OR = lambda a, b: a or b
LOGICAL_NOT = lambda a: not a

if __name__ == '__main__':
    x = True
    y = False
    
    result_and = LOGICAL_AND(x, y)
    result_or = LOGICAL_OR(x, y)
    result_not = LOGICAL_NOT(x)
    
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Logical AND ({x}, {y}): {result_and}")
    print(f"Logical OR ({x}, {y}): {result_or}")
    print(f"Logical NOT ({x}): {result_not}")