class BooleanOperators:
    def logical_and(self, a, b):
        return a and b
    
    def logical_or(self, a, b):
        return a or b
    
    def logical_not(self, a):
        return not a

if __name__ == '__main__':
    bo = BooleanOperators()
    sample_and = bo.logical_and(True, False)
    sample_or = bo.logical_or(False, True)
    sample_not = bo.logical_not(True)
    
    print(f"Logical AND (True, False): {sample_and}")
    print(f"Logical OR (False, True): {sample_or}")
    print(f"Logical NOT (True): {sample_not}")