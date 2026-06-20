class BooleanCombiner:
    @staticmethod
    def combine(ops, *bools):
        result = bools[0]
        for op, b in zip(ops, bools[1:]):
            if op == 'AND':
                result &= b
            elif op == 'OR':
                result |= b
            elif op == 'NOT':
                result = not b
        return result

if __name__ == '__main__':
    A = True
    B = False
    C = True
    result = BooleanCombiner.combine(['NOT', 'AND'], A, B, C)
    print(result)