class BooleanEvaluator:
    @staticmethod
    def both_false(x, y):
        return not x and not y

if __name__ == '__main__':
    x = False
    y = False
    result = BooleanEvaluator.both_false(x, y)
    print(result)