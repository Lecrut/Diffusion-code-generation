import operator

class LogicGateSystem:
    @staticmethod
    def AND(a, b):
        return operator.and_(a, b)
    
    @staticmethod
    def OR(a, b):
        return operator.or_(a, b)
    
    @staticmethod
    def NOT(a):
        return operator.not_(a)
    
    @staticmethod
    def XOR(a, b):
        return operator.xor(a, b)

if __name__ == '__main__':
    result_and = LogicGateSystem.AND(1, 0)
    result_or = LogicGateSystem.OR(1, 0)
    result_not = LogicGateSystem.NOT(1)
    result_xor = LogicGateSystem.XOR(1, 0)
    
    print(f"AND: {result_and}")
    print(f"OR: {result_or}")
    print(f"NOT: {result_not}")
    print(f"XOR: {result_xor}")