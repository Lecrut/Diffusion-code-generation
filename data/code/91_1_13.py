class BooleanHelper:
    @classmethod
    def is_valid_boolean(cls, value):
        return isinstance(value, bool)

    @classmethod
    def negate(cls, value):
        if cls.is_valid_boolean(value):
            return not value
        else:
            raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    negator = BooleanHelper()
    print(negator.negate(True))
    print(negator.negate(False))