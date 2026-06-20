class ComplexLogicSimulator:
    @staticmethod
    def evaluate_conditions(a, b, c, d):
        condition1 = (a & b) | (c & d)
        condition2 = (a | b) & (c | d)
        condition3 = a ^ b ^ c ^ d
        return condition1 or condition2 or condition3

if __name__ == '__main__':
    simulator = ComplexLogicSimulator()
    result = simulator.evaluate_conditions(1, 2, 3, 4)
    print(result)