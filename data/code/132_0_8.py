class LogicOperations:
    @staticmethod
    def evaluate_logic(a, b):
        return a & b

if __name__ == '__main__':
    result = LogicOperations.evaluate_logic(True, False)
    print(result)