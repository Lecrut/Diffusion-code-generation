import operator

class LogicGateSystem:
    AND = operator.and_
    OR = operator.or_
    NOT = operator.not_
    XOR = operator.xor
    
    @staticmethod
    def and_(a, b):
        return LogicGateSystem.AND(a, b)
    
    @staticmethod
    def or_(a, b):
        return LogicGateSystem.OR(a, b)
    
    @staticmethod
    def not_(a):
        return LogicGateSystem.NOT(a)
    
    @staticmethod
    def xor_(a, b):
        return LogicGateSystem.XOR(a, b)

if __name__ == '__main__':
    print(f"AND(1, 0): {LogicGateSystem.and_(1, 0)}")
    print(f"OR(1, 0): {LogicGateSystem.or_(1, 0)}")
    print(f"NOT(0): {LogicGateSystem.not_(0)}")
    print(f"XOR(1, 1): {LogicGateSystem.xor_(1, 1)}")