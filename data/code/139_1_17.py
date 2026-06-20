import operator

class LogicGateSystem:
    @staticmethod
    def and_(a, b):
        return operator.and_(a, b)
    
    @staticmethod
    def or_(a, b):
        return operator.or_(a, b)
    
    @staticmethod
    def not_(a):
        return operator.not_(a)
    
    @staticmethod
    def xor(a, b):
        return operator.xor(a, b)

if __name__ == '__main__':
    gate_system = LogicGateSystem()
    print(f"AND: {gate_system.and_(1, 0)}")
    print(f"OR: {gate_system.or_(1, 0)}")
    print(f"NOT 1: {gate_system.not_(1)}")
    print(f"XOR: {gate_system.xor(1, 0)}")