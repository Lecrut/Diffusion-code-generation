class BitwiseLogic:
    @staticmethod
    def evaluate_logic(a, b):
        return a & b

if __name__ == '__main__':
    logic_evaluator = BitwiseLogic()
    result = logic_evaluator.evaluate_logic(True, False)
    print(result)