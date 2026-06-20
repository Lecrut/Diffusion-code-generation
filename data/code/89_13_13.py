class LogicalConjunction:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    result = LogicalConjunction.evaluate(True, False)
    print(result)