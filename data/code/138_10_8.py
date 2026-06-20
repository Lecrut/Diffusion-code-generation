class BooleanOperations:
    @staticmethod
    def and_(a, b):
        return a and b

    @staticmethod
    def or_(a, b):
        return a or b

    @staticmethod
    def not_(a):
        return not a

    @staticmethod
    def nand(a, b):
        return not (a and b)

    @staticmethod
    def nor(a, b):
        return not (a or b)

    @staticmethod
    def xor(a, b):
        return a != b

    @staticmethod
    def xnor(a, b):
        return a == b

if __name__ == '__main__':
    bo = BooleanOperations()
    print("A | B | A AND B")
    print("---|---|---------")
    for A in [True, False]:
        for B in [True, False]:
            result_and = bo.and_(A, B)
            print(f"{A} | {B} | {result_and}")