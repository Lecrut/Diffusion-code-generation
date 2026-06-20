class LogicOperations:
    @staticmethod
    def check_or_condition(a: bool, b: bool) -> bool:
        return a | b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = LogicOperations.check_or_condition(sample_a, sample_b)
    print(result)