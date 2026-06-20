class LogicalConjunction:
    @staticmethod
    def evaluate_and(x: bool, y: bool) -> bool:
        return x and y

if __name__ == '__main__':
    sample1 = LogicalConjunction.evaluate_and(True, False)
    sample2 = LogicalConjunction.evaluate_and(False, True)
    print(sample1, sample2)