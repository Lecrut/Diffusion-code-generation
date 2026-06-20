class BooleanOperations:
    @classmethod
    def negate_boolean(cls, bool_val: bool) -> bool:
        return not bool_val

if __name__ == '__main__':
    negator = BooleanOperations()
    result1 = negator.negate_boolean(True)
    result2 = negator.negate_boolean(False)
    print(result1)
    print(result2)