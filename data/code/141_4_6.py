class BooleanCombiner:
    @staticmethod
    def and_combinator(a, b):
        return a and b

    @staticmethod
    def or_combinator(a, b):
        return a or b

    @staticmethod
    def not_combinator(a):
        return not a

    @staticmethod
    def evaluate(operators, *bools):
        result = bools[0]
        for op, b in zip(operators, bools[1:]):
            if op == 'AND':
                result = BooleanCombiner.and_combinator(result, b)
            elif op == 'OR':
                result = BooleanCombiner.or_combinator(result, b)
            elif op == 'NOT':
                result = BooleanCombiner.not_combinator(b)
        return result

if __name__ == '__main__':
    A = True
    B = False
    C = True
    result = BooleanCombiner.evaluate(['NOT', 'AND'], A, B, C)
    print(result)