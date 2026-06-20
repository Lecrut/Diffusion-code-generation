class LogicEvaluator:
    @staticmethod
    def logical_and(x: bool, y: bool) -> bool:
        return x and y

if __name__ == '__main__':
    result = LogicEvaluator.logical_and(True, False)
    print(result)