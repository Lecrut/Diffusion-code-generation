class BooleanLogicHandler:
    TRUE_CONSTANT = True
    FALSE_CONSTANT = False

    @classmethod
    def negate(cls, flag: bool) -> bool:
        if flag is cls.TRUE_CONSTANT:
            return cls.FALSE_CONSTANT
        if flag is cls.FALSE_CONSTANT:
            return cls.TRUE_CONSTANT
        raise ValueError("Input must be a boolean value")

if __name__ == '__main__':
    handler_instance = BooleanLogicHandler()
    true_result = handler_instance.negate(True)
    false_result = handler_instance.negate(False)
    print(true_result)
    print(false_result)